var CollectedSourcesListScoopit = (function() {

    var wrapper, sources = null;

    var signals = {
        'request': null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function buildListItem(object) {
        var id = object.id;
        var li = $(document.createElement('li'));
        li.attr('data-id', id);

        if(object.being_requested) {
            li.append('<span>(Being requested) ' + object.params.url + '</span> ');
        } else {
            li.append(
                '<a href="#" class="source">' + object.params.url + '</a>'
            );
        }
        li.append(
            ' <span>Last request on: ' +
               (object.last_request_date == null ? 'never' : object.last_request_date) +
            '</span>'
        );

        return li;
    }

    function buildList(objects) {
        var ul = $('<ul></ul>'),
            li;

        $.each(objects, function(id, object) {
            ul.append(buildListItem(object));
        });

        return ul;
    }

    function sourceRequested(source) {
    }

    function requestSource(id) {
        if(sources[id] === undefined) {
            throw 'Unknown source ' + id;
        }

        signals.request(sources[id], sourceRequested);
    }

    function render(sources_, wrapper_) {
        wrapper = wrapper_ || wrapper;
        sources = sources_ || sources;

        wrapper.empty();
        wrapper.off('click');

        wrapper.append(buildList(sources));

        wrapper.on('click', 'a.source', function(e) {
            e.preventDefault();
            var id = $(this).parent().attr('data-id');
            requestSource(id);
        });
    }

    return {
        connect: connect,
        render: render
    };
});
