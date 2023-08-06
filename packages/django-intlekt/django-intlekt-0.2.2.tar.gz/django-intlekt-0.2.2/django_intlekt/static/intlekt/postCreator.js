var PostCreator = (function() {

    var wrapper, collection, documents;

    var signals = {
        createDocument: null,
        createPost: null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function updateDocuments(documents_) {
        documents = documents_;
        var select = $('<select name="document"></select>');
        buildDocumentsSelect(select);
        wrapper.find('select[name="document"]').replaceWith(select);
    }

    function parseDocumentForm(form) {
        var doc = {};

        doc.id = form.find('*[name="id"]').val();
        doc.title = form.find('*[name="title"]').val().trim();
        doc.authors = Tools.commaStrToArray(form.find('*[name="authors"]').val());
        doc.created_on = form.find('*[name="created_on"]').val();
        doc.url = form.find('*[name="url"]').val();
        doc.keywords = Tools.commaStrToArray(form.find('*[name="keywords"]').val());
        doc.language = form.find('*[name="language"]').val();

        if(!doc.created_on) doc.created_on = null;
        if(!doc.language) doc.language = null;

        return doc;
    }

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

    function buildDocumentForm(form, object=null) {
        form.append('<label>Title:</label>');
        form.append('<input type="text" name="title" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Authors:</label>');
        form.append('<input type="text" name="authors" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Created on:</label>');
        form.append('<input type="date" name="created_on" placeholder="YYYY-MM-DD" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>URL:</label>');
        form.append('<input type="url" name="url" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Language:</label>');
        form.append('<input type="text" name="language" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Keywords:</label>');
        form.append('<input type="text" name="keywords" placeholder="keyword0, keyword1, ..." />');
        form.append(Tools.FIELD_ERRORS_HTML);

        if(object != null) {
            Tools.fillForm(object, form);
        }
    }

    function buildDocumentsSelect(select) {
        $.each(Tools.getUnlinkedDocuments(collection, documents), function(id, document_) {
            select.append(
                '<option value="' + id + '">' +
                    Tools.documentToStr(document_) +
                '</option>'
            );
        });
    }

    function buildPostForm(form, object=null) {
        form.append('<label>Document:</label>');
        var select = $('<select name="document"></select>');
        buildDocumentsSelect(select);
        form.append(select);
        form.append(' <a href="#" class="add-document"><i class="fa fa-plus" aria-hidden="true"></i></a>');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Collected on:</label>');
        form.append('<input type="date" name="collected_on" placeholder="YYYY-MM-DD" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Tags:</label>');
        form.append('<input type="text" name="tags" placeholder="tag0, tag1, ..." />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>URL:</label>');
        form.append('<input type="url" name="url" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Image:</label>');
        form.append('<input type="url" name="image" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Description:</label>');
        form.append('<textarea name="description"></textarea>');
        form.append(Tools.FIELD_ERRORS_HTML);

        if(object != null) {
            Tools.fillForm(object, form);
        }
    }

    function render(collection_, documents_ = null, wrapper_ = null) {
        wrapper = wrapper_ || wrapper;
        collection = collection_ || collection;
        documents = documents_ || documents;

        wrapper.empty();

        var documentForm = $('<form class="document-form"></form>');
        documentForm.append(
            '<a href="#" class="hide">' +
                '<i class="fa fa-minus" aria-hidden="true"></i>' +
            '</a><br/>'
        );
        buildDocumentForm(documentForm);
        documentForm.append('<input type="submit" value="Add" />');
        wrapper.append(documentForm);
        documentForm.hide();

        var postForm = $('<form class="post-form"></form>');
        buildPostForm(postForm);
        postForm.append('<input type="submit" value="Add" />');
        wrapper.append(postForm);

        postForm.submit(function(e) {
            e.preventDefault();
            signals.createPost(
                parsePostForm(postForm),
                collection,
                function(_) {
                    Tools.cleanFormFields(postForm);
                    Tools.cleanFormErrors(postForm);
                },
                function(errors) {
                    Tools.renderFormErrors(postForm, errors); 
                }
            );
        });

        postForm.on('click', 'a.add-document', function(e) {
            e.preventDefault();
            documentForm.show();
        });

        documentForm.on('click', 'a.hide', function(e) {
            e.preventDefault();
            documentForm.hide();
        });

        documentForm.submit(function(e) {
            e.preventDefault();
            signals.createDocument(
                parseDocumentForm(documentForm),
                function(document_) {
                    Tools.cleanFormFields(documentForm);
                    Tools.cleanFormErrors(documentForm);
                    documentForm.hide();
                    documents[document_.id] = $.extend(true, {}, document_);
                    updateDocuments(documents);
                },
                function(errors) {
                    Tools.renderFormErrors(documentForm, errors); 
                }
            );
        });
    }

    return {
        connect: connect,
        render: render,
        updateDocuments: updateDocuments
    };
});
