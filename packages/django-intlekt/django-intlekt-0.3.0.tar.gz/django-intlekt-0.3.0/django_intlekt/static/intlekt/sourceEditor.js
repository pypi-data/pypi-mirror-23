var SourceEditor = (function() {
    var collection = {};
    var id = null;

    var listOptions = {
        valueNames: ['source'] 
    };

    var wrapper = document.createElement('div');
    $(wrapper).append('<input type="text" class="search" placeholder="Search tag" />');
    $(wrapper).append('<button class="sort" data-sort="source">' +
                      'Sort by name' +
                      '</button>');
    $(wrapper).append('<ul></ul>');

    function render(collection_, parent_ = null, id_ = null) {
        collection = collection_ || collection;
        id = id_ || id;

        $.each(collection.sources, function(id, source) {
            $(wrapper).find('ul').append(
                '<li>' + source.name + ' <a href="#" class="hide">X</a></li>'
            );

        });

        if(parent_ && !$(parent_).find('#' + id).length) {
            parent_.appendChild(wrapper);
        }

        var list = new List(id, listOptions);
    }

    return {
        render: render
    };
});
