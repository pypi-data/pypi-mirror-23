var PostsList = (function() {
    var wrapper = null;
    var collection = {};
    var documents = {};
    var DEFAULT_POST_TITLE = 'Unknown title';

    var listOptions = {
        valueNames: ['documentName'] 
    };

    var signals = {};
    function connect(ev, cb) { signals[ev] = cb; }


    function addPost(post) {
        collection.posts[post.document] = $.extend(true, {}, post);
        var li = buildListItem(collection.posts[post.document]);
        wrapper.find('ul').append(li);
    }

    function postChanged(post) {
        collection.posts[post.document] = $.extend(true, {}, post);
        var li = buildListItem(collection.posts[post.document]);
        wrapper.find('li[data-id="' + post.document + '"]').replaceWith(li);
    }
    
    function documentChanged(document_) {
        documents[document_.id] = $.extend(true, {}, document_);
        var li = buildListItem(collection.posts[document_.id]);
        wrapper.find('li[data-id="' + document_.id + '"]').replaceWith(li);
    }

    function buildListItem(post) {
        var id = post.document;
        var li = $(document.createElement('li'));
        li.attr('data-id', id);

        if(!post.hidden) {
            li.append(
                '<a href="#" class="documentName" data-id="' + id + '">' + Tools.getPostTitle(post, documents) + '</a>' +
                '<a href="#" class="toggle-visibility hide" data-id="' + id + '">X</a>'
            );
        } else {
            li.append(
                '<span href="#" class="documentName">' + Tools.getPostTitle(post, documents) + '</span>' +
                '<a href="#" class="toggle-visibility show" data-id="' + id + '">O</a>'
            );
        }
        return li;
    }

    function buildList(posts) {
        var ul = $('<ul class="list"></ul>'),
            li;

        $.each(posts, function(id, post) {
            ul.append(buildListItem(post));
        });

        return ul;
    }

    function postSelected(collection, id) {
        wrapper.find('a.documentName').removeClass('selected');
        wrapper.find('li[data-id="' + id + '"]').addClass('selected');
    }

    function selectPost(id) {
        if(collection.posts[id] === undefined) {
            throw 'Unknown post ' + id;
        }

        signals.selectPost(collection, id, postSelected);
    }

    function render(collection_, documents_, wrapper_) {
        wrapper = wrapper_ || wrapper;
        collection = collection_ || collection;
        documents = documents_ || documents;

        wrapper.empty();

        wrapper.append('<input type="text" class="search" placeholder="Search post" />');
        wrapper.append(buildList(collection.posts));

        wrapper.off('click');
        wrapper.on('click', 'a.documentName', function(e) {
            e.preventDefault();
            var id = $(this).parent().attr('data-id');
            selectPost(id);
        });

        wrapper.on('click', 'a.toggle-visibility', function(e) {
            e.preventDefault();
            var id = $(this).parent().attr('data-id');

            if(collection.posts[id] === undefined) {
                throw 'Unknown post ' + id;
            }

            signals.togglePostVisibility(collection, id, postChanged);
        });

        new List(wrapper.attr('id'), listOptions);
    }

    return {
        addPost: addPost,
        connect: connect,
        documentChanged: documentChanged,
        postChanged: postChanged,
        postSelected: postSelected,
        render: render
    };
});
