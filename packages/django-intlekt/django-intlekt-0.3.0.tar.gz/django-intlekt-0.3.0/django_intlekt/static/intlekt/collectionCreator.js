var CollectionCreator = (function() {

    var wrapper;

    var signals = {
        createCollection: null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function parseForm(form) {
        var data = {};

        data.id = form.find('*[name="id"]').val();
        data.title = form.find('*[name="title"]').val().trim();
        data.curators = Tools.commaStrToArray(form.find('*[name="curators"]').val());

        return data;
    }

    function buildForm(object=null) {
        var form = $(document.createElement('form'));

        form.append('<label>Title:</label>');
        form.append('<input type="text" name="title" />');
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
        wrapper = wrapper_;

        wrapper.empty();
        var form = buildForm();
        form.append('<input type="submit" value="Create collection" />');
        wrapper.append(form);
        form.submit(function(e) {
            e.preventDefault();
            signals.createCollection(
                parseForm(form),
                function(_) {
                    Tools.cleanFormFields(form);
                    Tools.cleanFormErrors(form);
                },
                function(errors) {
                    Tools.renderFormErrors(form, errors); 
                }
            );
        });

    }

    return {
        connect: connect,
        render: render
    };
});
