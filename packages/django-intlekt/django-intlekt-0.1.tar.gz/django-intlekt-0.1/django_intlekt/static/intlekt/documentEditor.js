var DocumentEditor = (function() {
    var signals = {
        editDocument: null
    };
    function connect(signal, cb) { signals[signal] = cb; }

    var wrapper,
        document_;
    

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

    function documentChanged(changedDocument) {
        document_ = $.extend(true, {}, changedDocument);
    }

    function buildDocumentForm(document_ = null) {
        var form = $(document.createElement('form'));

        form.append('<input type="hidden" name="id" />');

        form.append('<label>Title:</label>');
        form.append('<input type="text" name="title" />');
        form.append(Tools.FIELD_ERRORS_HTML);
        
        form.append('<label>Authors (comma-separated):</label>');
        form.append('<input type="text" name="authors" placeholder="author1, author 2, ..." />');
        form.append(Tools.FIELD_ERRORS_HTML);
        
        form.append('<label>Created on:</label>');
        form.append('<input type="date" name="created_on" />');
        form.append(Tools.FIELD_ERRORS_HTML);
        
        form.append('<label>URL:</label>');
        form.append('<input type="url" name="url" />');
        form.append(Tools.FIELD_ERRORS_HTML);
        
        form.append('<label>Language:</label>');
        form.append('<input type="text" name="language" />');
        form.append(Tools.FIELD_ERRORS_HTML);
        
        form.append('<label>Keywords (comma-separated):</label>');
        form.append('<input type="text" name="keywords" placeholder="keyword1, keyword 2, ..." />');
        form.append(Tools.FIELD_ERRORS_HTML);
        
        if(document_ != null) {
            Tools.fillForm(document_, form);
        }

        return form;
    }

    function render(document__, wrapper_) {
        wrapper = wrapper_;
        document_ = document__;

        wrapper.empty();

        var documentForm = buildDocumentForm(document_);
        documentForm.append('<input type="submit" value="Update document" />');

        wrapper.append(documentForm);

        documentForm.submit(function(e) {
            e.preventDefault();
            signals.editDocument(
                parseDocumentForm(documentForm),
                documentChanged,
                function(errors) {
                    Tools.renderFormErrors(documentForm, errors); 
                    Tools.fillForm(document_, documentForm);
                }
            );
        });
    }

    return {
        connect: connect,
        documentChanged: documentChanged,
        render: render
    };
});
