var Breadcrumb = (function() {
    var wrapper;
    var collection = null, post = null, documents = null;

    var signals = {
        goToCollections: null,
        goToCollection: null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function setCollection(collection_, post_) {
        collection = collection_;
        if(post_ !== undefined) post = post_;
        render();
    }

    function setPost(post_) {
        if(collection == null) {
            throw 'Cannot set post without collection';
        }

        if(post_ == null) {
            post = null;
        } else {
            post = post_;
        }

        render();
    }

    function buildList() {
        var ul = $('<ul></ul>');

        ul.append('<li class="collections"><a href="#">Collections</a></li>');

        if(collection == null) return ul;

        ul.append(
            '<li><i class="fa fa-arrow-circle-right" aria-hidden="true"></i></li>' +
            '<li class="collection" data-id="' + collection.id + '">' +
            '<a href="#">' + collection.title + '</a>' +
            '</li>'
        );

        if(post == null) return ul;

        ul.append(
            '<li><i class="fa fa-arrow-circle-right" aria-hidden="true"></i></li>' +
            '<li class="post" data-id="' + post.document + '">' +
            Tools.getPostTitle(post, documents) +
            '</li>'
        );

        return ul;
    }

    function render(wrapper_, documents_) {
        wrapper = wrapper_ || wrapper;
        documents = documents_ || documents;

        wrapper.empty();
        wrapper.off('click');
        wrapper.append(buildList());

        wrapper.on('click', 'li.collections a', function(e) {
            e.preventDefault();
            signals.goToCollections(function() {
                collection = null;
                post = null;
                render();
            });
        });

        wrapper.on('click', 'li.collection a', function(e) {
            e.preventDefault();
            signals.goToCollection(collection, function() {
                post = null;
                render();
            });
        });
    }

    return {
        connect: connect,
        render: render,
        setCollection: setCollection,
        setPost: setPost
    };
});
