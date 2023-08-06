var CollectionsList = (function() {

    var wrapper, collections, currentCollection = null;

    var LIST_OPTIONS = {
        valueNames: ['collection-title'] 
    };

    var signals = {
        'selectCollection': null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function getCurrentCollection() {
        return currentCollection;
    }

    function buildListItem(object) {
        var id = object.id;
        var li = $(document.createElement('li'));
        li.attr('data-id', id);

        li.append(
            '<a href="#" class="collection-title">' + object.title + '</a>'
        );

        return li;
    }

    function buildList(objects) {
        var ul = $('<ul class="list"></ul>'),
            li;

        $.each(objects, function(id, object) {
            ul.append(buildListItem(object));
        });

        return ul;
    }

    function collectionSelected(collection) {
        wrapper.find('li').removeClass('selected');

        if(collection == null) {
            currentCollection = null;
            return;
        }

        if(collections[collection.id] === undefined) {
            throw 'Unknown collection ' + collection.id;
        }

        wrapper.find('li[data-id="' + collection.id + '"]').addClass('selected');
        currentCollection = collections[collection.id];
    }

    function selectCollection(id) {
        if(collections[id] === undefined) {
            throw 'Unknown collection ' + id;
        }

        signals.selectCollection(collections[id], collectionSelected);
    }

    function render(collections_, wrapper_) {
        wrapper = wrapper_ || wrapper;
        collections = collections_ || collections;

        wrapper.empty();
        wrapper.off('click');

        wrapper.append('<input type="text" class="search" placeholder="Search collection" />');
        wrapper.append(buildList(collections));

        wrapper.on('click', 'a.collection-title', function(e) {
            e.preventDefault();
            var id = $(this).parent().attr('data-id');
            selectCollection(id);
        });

        var list = new List(wrapper.attr('id'), LIST_OPTIONS);
        list.sort('collection-title', { order: "asc" });
    }

    return {
        collectionSelected: collectionSelected,
        connect: connect,
        getCurrentCollection: getCurrentCollection,
        render: render,
        selectCollection: selectCollection
    };
});
