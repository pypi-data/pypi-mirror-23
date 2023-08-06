var CollectionEditor = (function() {
    var wrapper, collection;

    var signals = {
        editCollection: null
    };
    function connect(signal, cb) { signals[signal] = cb; }
    
    function parseForm(form) {
        var data = {};

        data.id = form.find('*[name="id"]').val();
        data.title = form.find('*[name="title"]').val().trim();
        data.curators = Tools.commaStrToArray(form.find('*[name="curators"]').val());

        return data;
    }

    function buildForm(form, object) {
        form.append('<input type="hidden" name="id" />');

        form.append('<input type="text" name="title" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        form.append('<label>Curators:</label>');
        form.append('<input type="text" name="curators" />');
        form.append(Tools.FIELD_ERRORS_HTML);

        Tools.fillForm(object, form);
    }

    function buildDisplay(parent_, collection_) {
        parent_.append(
            '<h2>' +
                collection.title +
                ' <a href="#"><i class="fa fa-pencil" aria-hidden="true"></i></a>' +
            '</h2>'
        );
        parent_.append(
            '<div>' + Tools.listToCommaStr(collection.curators) + '</div>'
        );
        parent_.append(
            '<p>' +
                'Created on: ' + collection.created_on + '<br />' +
                'Updated on: ' + collection.updated_on +
            '</p>'
        );
    }

    function render(collection_, wrapper_) {
        wrapper = wrapper_ || wrapper;
        collection = collection_ || collection;

        wrapper.empty();
        
        var div = $(document.createElement('div'));
        buildDisplay(div);

        var form = $(document.createElement('form'));
        form.hide();
        buildForm(form, collection_);
        form.append('<input type="submit" value="Update the collection" />');

        wrapper.append(div);
        wrapper.append(form);

        div.on('click', 'a', function(e) {
            e.preventDefault();
            form.show(); 
            div.hide();
        });

        form.submit(function(e) {
            e.preventDefault();
            signals.editCollection(
                parseForm(form),
                function(collection) {
                    render(collection);
                },
                function(errors) {
                    Tools.renderFormErrors(form, errors); 
                }
            );
        });
    }

    function setWrapper(wrapper_) {
        wrapper = wrapper_;
    }

    return {
        connect: connect,
        render: render,
        setWrapper: setWrapper
    };
});
