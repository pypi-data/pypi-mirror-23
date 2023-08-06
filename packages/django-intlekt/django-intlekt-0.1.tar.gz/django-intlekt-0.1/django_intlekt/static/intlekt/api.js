var API = function(API_ROOT) {
    var module = {},
        cache = {
            'collections': null,
            'documents': null,
            'sources': null,
            'source_drivers': null,
            'tags': null
        };
    
    function cacheBuilderFactory(lookupField) {
        return function cacheBuilder(data) {
            var cache = {};

            for(let el of data) {
                cache[el[lookupField]] = el;
            }

            return cache;
        }
    }

    function list(name, cacheBuilder) {
        return function(success, error) {
            if (cache[name] != null) {
                return success(cache[name]);
            }

            $.ajax({
                url: API_ROOT + name + '/',
            })
            .done(function(data) {
                cache[name] = cacheBuilder(data); 
                success(cache[name]);
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                error(errorThrown, JSON.parse(jqXHR.responseText));
            });
        };
    }

    module.listCollections = list('intlekt/collections', cacheBuilderFactory('id'));
    module.listDocuments = list('intlekt/documents', cacheBuilderFactory('id'));
    module.listSources = list('intlekt/sources', cacheBuilderFactory('id'));
    module.listSourceDrivers = list('intlekt/source_drivers', cacheBuilderFactory('id'));
    module.listTags = list('intlekt/tags', cacheBuilderFactory('text'));
    module.listUSLs = list('intlekt/usls', cacheBuilderFactory('id'));

    function get(listFunction) {
        return function(id, success, error) {
            listFunction(function(data) {
                success(data[id]);
            }, error);
        };
    }

    module.getCollection = get(module.listCollections);
    module.getDocument = get(module.listDocuments);
    module.getSource = get(module.listSources);
    module.getSourceDriver = get(module.listSourceDrivers);
    module.getTag = get(module.listTags);

    function insert(name, lookupField, create) {
        return function(obj, success, error) {
            var url = API_ROOT + name + '/';
            if(!create)
                url += obj.id + '/';

            $.ajax({
                url: url,
                method: create ? 'POST' : 'PUT',
                data: JSON.stringify(obj),
                contentType: 'application/json'
            })
            .done(function(data) {
                if(cache[name][data[lookupField]] == undefined) {
                    cache[name][data[lookupField]] = {};
                }

                $.extend(true, cache[name][data[lookupField]], data);
                success(cache[name][data[lookupField]]);
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                error(errorThrown, JSON.parse(jqXHR.responseText));
            });
        };
    }
    
    function insertNestedFactory(name, lookupField) {
        return function(create) {
            return function(obj, collection, success, error) {
                var url = API_ROOT + 'intlekt/collections/' + collection.id + '/' + name + '/';
                if(!create)
                    url += obj[lookupField] + '/';

                $.ajax({
                    url: url,
                    method: create ? 'POST' : 'PUT',
                    data: JSON.stringify(obj),
                    contentType: 'application/json'
                })
                .done(function(data) {
                    if(cache.collections != null) {
                        if(cache['collections'][collection.id][name][data[lookupField]] == undefined) {
                            cache['collections'][collection.id][name][data[lookupField]] = {}; 
                        }
                        $.extend(
                            true,
                            cache['collections'][collection.id][name][data[lookupField]],
                            data
                        );
                    }
                    if(collection[name][data[lookupField]] == undefined) {
                        collection[name][data[lookupField]] = {}; 
                    }
                    $.extend(true, collection[name][data[lookupField]], data);
                    success(collection, data[lookupField]);
                })
                .fail(function(jqXHR, textStatus, errorThrown) {
                    error(errorThrown, JSON.parse(jqXHR.responseText));
                });
            };
        }
    }

    var insertPost = insertNestedFactory('posts', 'document');
    var insertCollectedSource = insertNestedFactory('sources', 'id');

    module.createCollection = insert('intlekt/collections', 'id', true);
    module.createDocument = insert('intlekt/documents', 'id', true);
    module.createTag = insert('intlekt/tags', 'text', true);
    module.createPost = insertPost(true);
    module.createCollectedSource = insertCollectedSource(true);

    module.updateCollection = insert('intlekt/collections', 'id', false);
    module.updateDocument = insert('intlekt/documents', 'id', false);
    module.updateTag = insert('intlekt/tags', 'text', false);
    module.updatePost = insertPost(false);
    module.updateCollectedSource = insertCollectedSource(false);

    module.requestSource = function(source, collection, success, error) {
        var params = $.extend(true, {}, source.params);
        params.collection_id = collection.id;
        params.source_id = source.id;

        module.getSourceDriver(source.driver, function(driver) {
            $.ajax({
                url: driver.url,
                method: 'POST',
                data: JSON.stringify(params),
                contentType: 'application/json'
            })
            .done(function(data) {
                source.last_request_date = new Date().toJSON().split('T')[0];
                source.being_requested = true;
                module.updateCollectedSource(source, collection, success, error);
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                error(errorThrown, JSON.parse(jqXHR.responseText));
            });
        }, error);
    };
    
    function delete_(name) {
        return function(id, success, error) {
            $.ajax({
                url: API_ROOT + name + '/' + id + '/',
                method: 'DELETE',
            })
            .done(function(resp) {
                delete cache[name][id];
                success(resp);
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                error(errorThrown, JSON.parse(jqXHR.responseText));
            });
        };
    }

    module.deleteTag = delete_('intlekt/tags');

    module.textsToTags = function(texts, success, error) {
        module.listTags(function(tags) {
            var tag;
            var selectedTags = {};

            for(let text of texts) {
                for(let tagText in tags) {
                    tag = tags[tagText];

                    if(tag.text == text) {
                        selectedTags[text] = tag;
                        break;
                    }
                }
                if(selectedTags[text] == undefined) {
                    selectedTags[text] = {
                        text: text,
                        id: '',
                        usls: []
                    };
                }
            }

            success(selectedTags);
        }, error);
    }

    return module;
};
