var CollectedSourceCreatorScoopit = (function() {

    var wrapper, collection, driverId;

    var signals = {
        createCollectedSource: null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function parseForm(form) {
        var data = {params: {}};

        data.driver = form.find('*[name="driver"]').val().trim();
        data.params.url = form.find('*[name="url"]').val().trim();

        return data;
    }
    
    function buildForm() {
        var form = $(document.createElement('form'));

        form.append('<input type="hidden" name="driver" value="' + driverId + '" />');

        form.append('<label>URL:</label>');
        form.append('<input type="url" name="url" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        return form;
    }

    function render(wrapper_, collection_, driverId_) {
        wrapper = wrapper_ || wrapper;
        collection = collection_ || collection;
        driverId = driverId_ || driverId;

        wrapper.empty();

        var form = buildForm();
        form.append('<input type="submit" value="Add" />');
        wrapper.append(form);

        form.submit(function(e) {
            e.preventDefault();
            signals.createCollectedSource(
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
