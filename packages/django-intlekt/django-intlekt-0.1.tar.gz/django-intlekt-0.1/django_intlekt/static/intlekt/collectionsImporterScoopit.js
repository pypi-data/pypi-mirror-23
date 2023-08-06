var CollectionsImporterScoopit = (function() {

    var wrapper;

    var signals = {
        importCollection: null,
        importUserCollections: null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function parseURLForm(form) {
        var data = {};

        data.url = form.find('*[name="url"]').val().trim();
        data.curators = Tools.commaStrToArray(form.find('*[name="curators"]').val());

        return data;
    }
    
    function parseUserForm(form) {
        var data = {};

        data.user = form.find('*[name="user"]').val().trim();
        data.curators = Tools.commaStrToArray(form.find('*[name="curators"]').val());

        return data;
    }
    
    function buildUserForm(object=null) {
        var form = $(document.createElement('form'));

        form.append('<label>User:</label>');
        form.append('<input type="text" name="user" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Curators:</label>');
        form.append('<input type="text" name="curators" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        if(object != null) {
            Tools.fillForm(object, form);
        }

        return form;
    }

    function buildURLForm(object=null) {
        var form = $(document.createElement('form'));

        form.append('<label>URL:</label>');
        form.append('<input type="url" name="url" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Curators:</label>');
        form.append('<input type="text" name="curators" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        if(object != null) {
            Tools.fillForm(object, form);
        }

        return form;
    }

    function render(wrapper_) {
        wrapper = wrapper_ || wrapper;

        wrapper.empty();

        var urlForm = buildURLForm();
        urlForm.append('<input type="submit" value="Import collection" />');
        wrapper.append(urlForm);

        var userForm = buildUserForm();
        userForm.append('<input type="submit" value="Import user collections" />');
        wrapper.append(userForm);

        urlForm.submit(function(e) {
            e.preventDefault();
            signals.importCollection(
                parseURLForm(urlForm),
                function(_) {
                    Tools.cleanFormFields(urlForm);
                    Tools.cleanFormErrors(urlForm);
                },
                function(errors) {
                    Tools.renderFormErrors(urlForm, errors); 
                }
            );
        });
        
        userForm.submit(function(e) {
            e.preventDefault();
            signals.importUserCollections(
                parseUserForm(userForm),
                function(_) {
                    Tools.cleanFormFields(userForm);
                    Tools.cleanFormErrors(userForm);
                },
                function(errors) {
                    Tools.renderFormErrors(userForm, errors); 
                }
            );
        });
    }

    return {
        connect: connect,
        render: render
    };
});
