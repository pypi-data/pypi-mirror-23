var USLEditor = (function() {

    var wrapper, collection, documents;

    var signals = {
        updateUSL: null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function parseForm(form) {
        var p = {};
        
        p.document = form.find('*[name="document"]').val();
        p.usl = form.find('*[name="usl"]').val();

        if(!p.usl) p.usl = null;

        return p;
    }

    function buildForm(form, object) {
        form.append('<label>USL:</label>');
        form.append('<input type="text" name="usl" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        if(object !== undefined) {
            Tools.fillForm(object, form);
        }
    }

    function render(wrapper_) {
        wrapper = wrapper_ || wrapper;

        wrapper.empty();

        var form = $(document.createElement('form'));
        buildForm(form);
        form.append('<input type="submit" value="Update" />');
        wrapper.append(form);

        form.submit(function(e) {
            e.preventDefault();
            signals.updateUSL(
                parseForm(form),
                function() {

                },
                function(error) {

                }
            );
        });
    }

    return {
        connect: connect,
        render: render
    };
});
