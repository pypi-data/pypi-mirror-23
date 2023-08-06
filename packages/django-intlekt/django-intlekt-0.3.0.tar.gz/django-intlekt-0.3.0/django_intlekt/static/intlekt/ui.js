$(function() {
    
    // Globals
    
    var API_ROOT = 'http://127.0.0.1:8000/';
    var SCOOPIT_DRIVER_ID = '59512a14b15ab31709c0e00b';
    var USL_CONCAT_CHAR = '+';

    var api = API(API_ROOT);
    var collectionTagEditor = TagEditor();
    var postTagEditor = TagEditor();
    var documentEditor = DocumentEditor();
    var postEditor = PostEditor();
    var postsList = PostsList();
    var postCreator = PostCreator();
    var collectionsList = CollectionsList();
    var collectionsImporterScoopit = CollectionsImporterScoopit();
    var collectionCreator = CollectionCreator();
    var collectionEditor = CollectionEditor();
    var collectedSourceCreatorScoopit = CollectedSourceCreatorScoopit();
    var collectedSourcesListScoopit = CollectedSourcesListScoopit();
    var breadcrumb = Breadcrumb();

    var collections = {},
        documents = {};

    Tabs($('#collection'));
    Tabs($('#post'));

    collectionEditor.setWrapper($('#collection-editor'));

    function documentChanged(document_) {
        documents[document_.id] = documents[document_.id] || {};
        $.extend(true, documents[document_.id], document_);
        breadcrumb.render();
        postsList.render();
    }

    function collectedSourceChanged(source, collection) {
        collections[collection.id].sources[source.id] = collections[collection.id].sources[source.id] || {};
        $.extend(true, collections[collection.id].sources[source.id], source);
        collectedSourcesListScoopit.render();
    }

    function postChanged(post, collection) {
        collections[collection.id].posts[post.document] = collections[collection.id].posts[post.document] || {};
        $.extend(true, collections[collection.id].posts[post.document], post);
        
        postEditor.render();
        postsList.render();
        
        api.textsToTags(
            Tools.getCollectionTextTags(collection),
            function(tags) {
                collectionTagEditor.render(tags);
                var postTags = {};
                $.each(tags, function(text, tag) {
                    if(post.tags.indexOf(text) == -1) return;
                    postTags[text] = tag;
                });
                postTagEditor.render(postTags);
            },
            function(err, details) {
                displayError('Unable to load tags: ' + err);
            }
        );
    }

    function collectionChanged(collection) {
        collections[collection.id] = collections[collection.id] || {};
        $.extend(true, collections[collection.id], collection);
        collectionsList.render();
        breadcrumb.render();
        collectionEditor.render();
    }

    function selectCollection(collection) {
        cleanMessages();

        api.listUSLs(
            function(usls) {
                api.textsToTags(
                    Tools.getCollectionTextTags(collection),
                    function(tags) {
                        collectionTagEditor.render(tags, $('#collection-tag-editor'), usls);
                    },
                    function(err, details) {
                        displayError('Unable to load tags: ' + err);
                    }
                );
            },
            function(err, details) {
                displayError('Unable to load USLs: ' + err);
            }
        );

        api.listDocuments(function(documents) {
            $('#post').hide();
            $('#collection').show();
            $('#collections').hide();
            collectionsList.collectionSelected(collection);
            breadcrumb.setCollection(collection, null);
            breadcrumb.render();
            collectionEditor.render(collection, $('#collection-editor'));
            postCreator.render(collection, documents, $('#post-creator'));
            postsList.render(
                collection,
                documents,
                $('#posts-list')
            );
        }, function(err, details) {
            displayError('Unable to load documents: ' + err);
        });

        collectedSourceCreatorScoopit.render($('#collected-source-creator-scoopit'), collection, SCOOPIT_DRIVER_ID);
        collectedSourceCreatorScoopit.connect(
            'createCollectedSource',
            function(params, success, error) {
                api.createCollectedSource(
                    params,
                    collectionsList.getCurrentCollection(),
                    function(collection, id) {
                        collectedSourceChanged(collection.sources[id], collection);
                        success(collection.sources[id]);
                    }, function(err, details) {
                        displayError('Unable to load source driver: ' + err);
                    }
                );
            }
        );

        collectedSourcesListScoopit.render(collection.sources, $('#collected-sources-list-scoopit'));
    }
    
    function selectPost(collection, id) {
        cleanMessages();
        var post = collection.posts[id];
        /*
        postUSLs(
            post,
            renderUSLBuilder,
            function(err, details) {
                displayErrors('Unable to build USL hint: ' + err);
            }
        );
        */
        api.listUSLs(
            function(usls) {
                api.textsToTags(
                    post.tags,
                    function(tags) {
                        postTagEditor.render(tags, $('#post-tag-editor'), usls);
                    },
                    function(err, details) {
                        displayError('Unable to load tags: ' + err);
                    }
                );
            },
            function(err, details) {
                displayError('Unable to load USLs: ' + err);
            }
        );

        api.getDocument(
            post.document,
            function(document_) {
                postEditor.render(post, document_, $('#post-editor'));
                documentEditor.render(document_, $('#document-editor'));
                $('#post').show();
                $('#collection').hide();
                $('#collections').hide();
                postsList.postSelected(post);
                breadcrumb.setPost(post);
            },
            function(err, details) {
                displayError('Unable to load document: ' + err);
            }
        );
    }

    api.listDocuments(function(documents) {
        breadcrumb.render($('nav'), documents);
    }, function(err, details) {
        displayError('Unable to load documents: ' + err);
    });
    breadcrumb.connect('goToCollections', function(cb) {
        cleanMessages();
        $('#collection').hide();
        $('#post').hide();
        $('#collections').show();
        collectionsList.collectionSelected(null);
        cb();
    });
    breadcrumb.connect('goToCollection', selectCollection);


    collectionCreator.render($('#collection-creator'));
    collectionCreator.connect('createCollection', function(collection, success, error) {
        cleanMessages();
        api.createCollection(
            collection,
            function(collection) {
                collectionChanged(collection);
                success(collection);
            },
            function(err, details) {
                displayError('Unable to create collection: ' + err);
                error(details);
            }
        );       
    });

    function importCb(params, success, error) {
        params.driver = SCOOPIT_DRIVER_ID;
        api.getSourceDriver(SCOOPIT_DRIVER_ID, function(driver) {
            $.ajax({
                url: driver.url,
                method: 'POST',
                data: JSON.stringify(params),
                contentType: 'application/json'
            })
            .done(success)
            .fail(function(jqXHR, textStatus, errorThrown) {
                displayError('Unable to request source: ' + errorThrown);
                error(JSON.parse(jqXHR.responseText));
            });
        }, function(err, details) {
                displayError('Unable to load source driver: ' + err);
                error(details);
        });
    }

    collectionsImporterScoopit.render($('#collections-importer-scoopit'));
    collectionsImporterScoopit.connect('importCollection', importCb);
    collectionsImporterScoopit.connect('importUserCollections', importCb);


    collectionsList.connect('selectCollection', selectCollection);

    
    collectionEditor.connect('editCollection', function(collection, success, error) {
        cleanMessages();
        api.updateCollection(collection, function(collection) {
            collectionChanged(collection);
        }, function(err, details) {
            displayError('Unable to update post: ' + err);
            error(details);
        });
    });
    

    postCreator.connect('createPost', function(post, collection, success, error) {
        cleanMessages();
        api.createPost(
            post,
            collection,
            function(collection) {
                success(collection);
                postCreator.render(collection);
                postsList.addPost(collection.posts[post.document]);
            },
            function(err, details) {
                displayError('Unable to create document: ' + err);
                error(details);
            }
        );       
    });
    
    postCreator.connect('createDocument', function(document_, success, error) {
        cleanMessages();
        api.createDocument(
            document_,
            function(document_) {
                success(document_);
            },
            function(err, details) {
                displayError('Unable to create document: ' + err);
                error(details);
            }
        );       
    });


    postsList.connect('selectPost', function(collection, document_, cb) {
        selectPost(collection, document_);
        cb();
    });

    postsList.connect('togglePostVisibility', function(collection, document_, cb) {
        var post = collection.posts[document_];
        post.hidden = !post.hidden;
        
        api.updatePost(post, collection, function(collection) {
            if(post.hidden) {
                $('#post').hide();
            }

            cb(collection.posts[post.document]);
        }, function(err, details) {
            displayError('Unable to update document: ' + err);
        });
    });


    collectedSourcesListScoopit.connect('request', function(source, success, error) {
        api.requestSource(
            source, collectionsList.getCurrentCollection(),
            function(collection) {
                collectedSourceChanged(
                    collection.sources[source.id],
                    collection
                );
                success(collection.sources[source.id]);
            },
            function(err, details) {
                displayError('Unable to request source: ' + err);
                error(details);
            }
        );
    });


    postEditor.connect('editPost', function(post, success, error) {
        cleanMessages();
        api.updatePost(post, collectionsList.getCurrentCollection(), function(collection) {
            postChanged(collection.posts[post.document], collection);
            success(collection.posts[post.document], collection);
        }, function(err, details) {
            displayError('Unable to update post: ' + err);
            error(details);
        });
    });
    
    documentEditor.connect('editDocument', function(document_, success, error) {
        cleanMessages();
        api.updateDocument(document_, function(document_) {
            documentChanged(document_);
            success(document_);
        }, function(err, details) {
            displayError('Unable to update document: ' + err);
            error(details);
        });
    });

    function unlinkUSL(usl, tag, success, error) {
        if(!tag.id) {
            error('Cannot remove an USL to the tag ' + tag.text);
        }
        var index = tag.usls.indexOf(usl);
        if(index == -1) {
            error('Cannot remove the USL ' + usl + ' to the tag ' + tag.text);
        }

        tag.usls.splice(index, 1);

        // No USLS anymore, delete tag
        if(tag.usls.length == 0) {
            api.deleteTag(tag.id, function() {
                success(Tools.createTag(tag.text)); 
            }, error);
            return;
        }
        
        api.updateTag(tag, success, error);
    }
    
    collectionTagEditor.connect('unlinkUSL', unlinkUSL);
    postTagEditor.connect('unlinkUSL', unlinkUSL);
    
    function linkUSL(usl, tag, success, error) {
        if(tag.usls.indexOf(usl) != -1) {
            return error('The USL is already linked to the tag.');
        }

        tag.usls.push(usl);
        var apiCall;

        if(!tag.id) {
            delete tag.id;
            apiCall = api.createTag;
        } else {
            apiCall = api.updateTag;
        }

        apiCall(tag, success, function(err, details) {
            displayError('Unable to update tag: ' + err);
            error(details);
        });
    }

    collectionTagEditor.connect('linkUSL', linkUSL);
    postTagEditor.connect('linkUSL', linkUSL);


    // Helpers
    
    function listToStr(list) {
        return list.join(', ');
    }

    var authorsToStr = listToStr;
    var keywordsToStr = listToStr;

    function strToArray(str) {
        var array = str.split(',').map(function(s) { return s.trim(); });
        // If str is an empty string, array == [''], but we want []
        return !array[0] ? [] : array;
    }

    var authorsToArray = strToArray;
    var tagsToArray = strToArray;
    var keywordsToArray = strToArray;

    function postUSLs(post, success, error) {
        api.listTags(function(tags) {
            var usls = {};

            for(let text of post.tags) {
                if(tags[text] != undefined) {
                    usls[text] = tags[text].usls;
                } else {
                    usls[text] = [];
                }
            }

            success(usls);
        }, error);
    }

    function collectedSourceToStr(collectedSource, callback) {
        api.getSourceDriver(
            collectedSource.driver,
            function(driver) {
                api.getSource(
                    driver.source,
                    function(source) {
                        var str = source.name + ' (';
        
                        if (driver.id == SCOOPIT_DRIVER_ID) {
                            if (collectedSource.params.url != undefined)
                                str += collectedSource.params.url;
                            else if (collectedSource.params.user != undefined)
                                str += collectedSource.params.user;
                        }

                        str += ')';

                        callback(str);
                    },
                    function(err, details) {
                        displayError('Unable to load source: ' + err);
                    }
                );
            },
            function(err, details) {
                displayError('Unable to load source driver: ' + err);
            }
        );
    }

    function textToTag(text, success, error) {
        api.getTag(
            text,
            function(tag) {
                if(tag) {
                    return success(tag);
                }

                return success(createTag(text));
            },
            function(err, details) {
                error(err, details);
            }
        );
    }

    function removeUSLFromTag(usl, tag, success, error) {
        if(!tag.id) {
            throw 'Cannot remove an USL to the tag ' + tag.text;
        }
        var index = tag.usls.indexOf(usl);
        if(index == -1) {
            throw 'Cannot remove an USL to the tag ' + tag.text;
        }

        tag.usls.splice(index, 1);

        // No USLS anymore, delete tag
        if(tag.usls.length == 0) {
            api.deleteTag(tag.id, success, error);
            return;
        }
        
        api.updateTag(tag, success, error);
    }

    // Renderers

    function renderSourceList(collection) {
        var li, a, source;
        $('#collection-sources').empty();

        for(let i in collection.sources) {
            source = collection.sources[i];

            li = document.createElement('li');

            a = document.createElement('a');
            a.setAttribute('href', '');

            (function(a, source) {
                collectedSourceToStr(source, function(str) {
                    a.innerHTML = str;
                });
            })(a, source);

            (function(source) {
                $(a).click(function(e) {
                    e.preventDefault();

                    api.getSourceDriver(
                        source.driver,
                        function(driver) {
                            api.requestSource(
                                collection,
                                driver,
                                source.params,
                                function(resp) {
                                    displayMessage('Source being collected... Reload the page to see new documents.');
                                },
                                function(err, details) {
                                    displayError('Unable to request source: ' + err);
                                }
                            );
                        },
                        function(err, details) {
                            displayError('Unable to load source driver: ' + err);
                        }
                    );
                });
            })(source);

            li.appendChild(a);

            a = document.createElement('a');
            a.setAttribute('href', '');
            a.setAttribute('class', 'hide');
            a.innerHTML = 'X';

            (function(i) {
                $(a).click(function(e) {
                    e.preventDefault();

                    collection.sources.splice(i, 1);
                    api.updateCollection(
                        collection,
                        function(collection) {
                            renderSourceList(collection);
                            displayMessage('Source unlinked successfully!');
                        },
                        function(err, details) {
                            displayError('Unable to unlink source: ' + err);
                            displayFormErrors(form, details);
                        }
                    );
                });
            })(i);

            li.appendChild(a);
            $('#collection-sources').append(li);
        }
    }

    function renderCollectionForm(collection) {
        $('#edit-collection-form input[name="id"]').val(collection.id);
        $('#edit-collection-form input[name="title"]').val(collection.title);
        $('#edit-collection-form input[name="authors"]').val(authorsToStr(collection.authors));
    }

    function renderCollection(collection) {
        if(collection == null) return;

        currentCollection = collection;

        $('#collection-created-on span').html(collection.created_on);
        $('#collection-updated-on span').html(collection.updated_on);

        renderCollectionForm(collection);
        renderSourceList(collection);
        api.listDocuments(function(documents) {
            postsList.render(
                collection,
                documents,
                $('#posts-list')
            );
        });
        // renderDocumentList(collection);
        api.textsToTags(
            collectionTagTexts(collection),
            renderTagEditor,
            function(err, details) {
                displayError('Unable to load tags: ' + err);
            }
        );
        
        $('#post').hide();
        $('#add-document').hide();
        $('#add-source').hide();
        $('#tag-editor').hide();
        $('#collection').show();
        $('#collection').data('id', collection.id);
    }

    function renderUSLBuilder(usls) {
        var builder = USLBuilder(usls, USL_CONCAT_CHAR);
        var els = builder.render();
        $('#usl-hint').empty();
        $('#usl-hint').append(els.hintDiv);
        $('#usl-hint').append(els.table);
    }

        
    function renderDocumentForm(doc) {
        var form = $('#edit-document-form');

        for(let key in doc) {
            form.find('*[name="' + key + '"]').val(doc[key]);
        }
        form.find('*[name="authors"]').val(authorsToStr(doc.authors));
        form.find('*[name="keywords"]').val(keywordsToStr(doc.keywords));
    }


    function renderCollectDocumentForm() {
        api.listDocuments(function(documents) {
            var docs = unlinkedDocuments(currentCollection, documents);

            var select = $('#collect-document-form select');
            select.empty();

            var option, doc;
            
            option = document.createElement('option');
            option.setAttribute('value', '');
            select.append(option);

            for(let docId of docs) {
                doc = documents[docId];

                option = document.createElement('option');
                option.setAttribute('value', doc.id);
                option.innerHTML = doc.title;

                select.append(option);
            }
        }, function(err, details) {
            displayError('Unable to load documents: ' + err);
        });
    }
    
    function displayFormErrors(form, errors) {
        var errDiv;

        for(let fieldName in errors) {
            errDiv = form.find('*[name="' + fieldName + '"]').next('div');
            errDiv.html(errors[fieldName]);
        }
    }

    function displayMessage(msg) {
        $('#messages').html(msg);
    }

    displayError = displayMessage;

    function cleanMessages() {
        $('#messages').html('');
    }
    
    function cleanFormErrors(form) {
        form.find('.field-errors').html('');
    }

    function cleanFormFields(form) {
        form.find('input[type!="submit"], textarea').val('');
    }

    function cleanForm(form) {
        cleanFormFields(form);
        cleanFormErrors(form);
    }

    // Parsers

    function parseAddUSLForm(form) {
        var data = {};

        data.usl = form.find('*[name="usl"]').val().trim();

        return data;
    }

    function parseAddScoopitByUrlForm(form) {
        var params = {};

        params.url = form.find('*[name="url"]').val();

        return params;
    }
    
    function parseAddScoopitByUserForm(form) {
        var params = {};

        params.user = form.find('*[name="user"]').val();

        return params;
    }
    
    // Events

    $('form').submit(function(e) {
        cleanFormErrors($(this));
        cleanMessages();
    });

    $('#create-collection form').submit(function(e) {
        e.preventDefault();
        var form = $(this);

        api.createCollection(
            parseCollectionForm(form),
            function(data) {
                collections[data.id] = data;
                cleanForm(form);
                $('#create-collection').hide();

                renderCollection(data);
                renderCollectionList();
                displayMessage('Collection created successfully!');
            },
            function(err, details) {
                displayError('Unable to create collection: ' + err);
                displayFormErrors(form, details);
            }
        );
    });
    
    $('#edit-collection-form').submit(function(e) {
        e.preventDefault();
        var form = $(this);

        api.updateCollection(
            parseCollectionForm(form),
            function(data) {
                api.listCollections(
                    renderCollectionList,
                    function(err, details) {
                        displayError('Unable to load collections: ' + err);
                    }
                );
                renderCollection(data);
                displayMessage('Collection updated successfully!');
            },
            function(err, details) {
                displayError('Unable to update collection: ' + err);
                displayFormErrors(form, details);
            }
        );
    });

    $('#collect-document-form').submit(function(e) {
        e.preventDefault();
        var form = $(this);

        cleanFormErrors(form);
        var parsedForm = parseCollectDocumentForm(form);
        var doc = parsedForm.doc;
        var post = parsedForm.post;

        function createDocumentCallback(doc) {
            post.document = doc.id;

            api.createPost(
                post,
                currentCollection,
                function(collection) {
                    currentCollection = collection;
                    renderDocumentList(collection);
                    renderPost(doc.id, collection);
                    cleanForm(form);
                    displayMessage('Document collected successfully!');
                    $('#collect-document').hide();
                },
                function(err, details) {
                    displayError('Unable to create document: ' + err);
                    displayFormErrors(form, details);
                }
            );
        }

        if(doc.id != '') {
            api.getDocument(
                doc.id,
                createDocumentCallback,
                function(err, details) {
                    displayError('Unable to load document: ' + err);
                }
            );
        }
        else {
            api.createDocument(
                doc,
                createDocumentCallback,
                function(err, details) {
                    displayError('Unable to create document: ' + err);
                    displayFormErrors(form, details);
                }
            );
        }
    });
    
    $('#edit-post-form').submit(function(e) {
        e.preventDefault();

        var form = $(this);
        var post = parsePostForm(form);

        api.updatePost(post, currentCollection, function(collection) {
            currentCollection = collection;
            cleanForm(form);
            renderPost(post.document, currentCollection);
            displayMessage('Post updated successfully!');
        }, function(err, details) {
            displayError('Unable to update document: ' + err);
            displayFormErrors(form, details);
        });
    });
    
    $('#edit-document-form').submit(function(e) {
        e.preventDefault();

        var form = $(this);
        var data = parseDocumentForm(form);

        api.updateDocument(data, function(doc) {
            cleanFormErrors(form);
            displayMessage('Document updated successfully!');
        }, function(err, details) {
            displayError('Unable to update document: ' + err);
            displayFormErrors(form, details);
        });
    });

    $('#add-collection-button').click(function(e) {
        $('#create-collection').toggle();
    });

    $('#add-source-button').click(function(e) {
        $('#add-source').toggle();
    });

    $('#tag-editor-button').click(function(e) {
        $('#tag-editor').toggle();
    });

    $('#collect-document-button').click(function(e) {
        renderCollectDocumentForm();
        $('#collect-document').toggle();
    });

    function addSourceFactory(form, driver, parser) {
        form.submit(function(e) {
            e.preventDefault();

            var source = {
                driver: driver,
                params: parser(form) 
            };
            currentCollection.sources.push(source);

            api.updateCollection(currentCollection, function(collection) {
                cleanForm(form);
                renderSourceList(collection);
                displayMessage('Source added successfully!');
            }, function(err, details) {
                displayError('Unable to add source: ' + err);
                displayFormErrors(form, details);
            });
        });
    }

    addSourceFactory(
        $('#add-scoopit-url-source-form'),
        SCOOPIT_DRIVER_ID,
        parseAddScoopitByUrlForm
    );

    addSourceFactory(
        $('#add-scoopit-user-source-form'),
        SCOOPIT_DRIVER_ID,
        parseAddScoopitByUserForm
    );

    // Init

    api.listCollections(function(collections_) {
        collections = collections_;
        collectionsList.render(collections, $('#collections-list'));

        $('#messages').html('');
        $('#collections').show();
    }, function(err) {
        displayError('Unable to load collections: ' + err); 
    });
});
