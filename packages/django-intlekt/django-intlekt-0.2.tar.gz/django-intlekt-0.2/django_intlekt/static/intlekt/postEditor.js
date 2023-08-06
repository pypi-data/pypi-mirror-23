var PostEditor = (function() {
    var signals = {
        editPost: null,
    };
    function connect(signal, cb) { signals[signal] = cb; }

    var wrapper,
        post,
        document_;
    

    function parsePostForm(form) {
        var p = {};
        
        p.document = form.find('*[name="document"]').val();
        p.collected_on = form.find('*[name="collected_on"]').val();
        p.url = form.find('*[name="url"]').val();
        p.tags = Tools.commaStrToArray(form.find('*[name="tags"]').val());
        p.image = form.find('*[name="image"]').val();
        p.description = form.find('*[name="description"]').val();

        if(!p.collected_on) p.collected_on = new Date().toJSON().split('T')[0];
        if(!p.image) p.image = null;
        if(!p.url) p.url = null;

        return p;
    }

    function postChanged(changedPost) {
        post = changedPost;
    }

    function documentChanged(changedDocument) {
        document_ = $.extend(true, {}, changedDocument);
    }

    function buildPostForm(post = null) {
        var form = $(document.createElement('form'));

        form.append('<input type="hidden" name="document" />');

        form.append('<label>Collected on:</label>');
        form.append('<input type="date" name="collected_on" />');
        form.append('<div class="field-errors"></div>');

        form.append('<label>Tags (comma-separated):</label>');
        form.append('<input type="text" name="tags" placeholder="tag0, tag 1, ..." />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Image:</label>');
        form.append('<input type="url" name="image" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>URL:</label>');
        form.append('<input type="url" name="url" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Description:</label>');
        form.append('<textarea name="description"></textarea>');
        form.append(Tools.FIELD_ERRORS_HTML);

        if(post != null) {
            Tools.fillForm(post, form);
        }

        return form;
    }

    function render(post_, document__, wrapper_) {
        wrapper = wrapper_ || wrapper;
        post = post_ || post;
        document_ = document__ || document_;

        wrapper.empty();

        var postForm = buildPostForm(post);
        postForm.append('<input type="submit" value="Update post" />');

        wrapper.append(postForm);

        postForm.submit(function(e) {
            e.preventDefault();
            signals.editPost(
                parsePostForm(postForm),
                postChanged,
                function(errors) {
                    Tools.renderFormErrors(postForm, errors); 
                    Tools.fillForm(post, postForm);
                }
            );
        });
    }

    return {
        connect: connect,
        postChanged: postChanged,
        render: render
    };
});
