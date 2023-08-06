var TagEditor = (function() {
    var USL_AUTOCOMPLETE_MIN_LEN = 3;

    var wrapper;
    var tags, usls = {};
    var id = null;

    var LIST_OPTIONS = {
        valueNames: ['tag', 'usl'] 
    };
    
    var signals = {
        unlinkUSL: null,
        linkUSL: null
    };
    function connect(ev, cb) { signals[ev] = cb; }

    function updateTag(tag) {
        tags[tag.text] = $.extend(true, {}, tag);
        render(tags);
    }

    function iemlToUSLId(ieml) {
        for(let usl in usls) {
            if(usls[usl].ieml_text == ieml) {
                return usl;
            }
        }

        return '';
    }

    function buildLinkUSLForm(tag) {
        var form = $(document.createElement('form'));
        form.data('tag-text', tag.text);

        form.append('<input type="text" class="link-usl" />');
        form.append('<input type="submit" value="Link" />');
        form.append('<div class="field-errors"></div>');

        return form;
    }

    function buildUSLList(tag) {
        var ul = $(document.createElement('ul'));
        var li, child;

        for(let uslId of tag.usls) {
            li = $(document.createElement('li'));
            
            li.append('<span class="usl">' + usls[uslId].ieml_text + '</span>');
            $('<a href="#" class="hide">X</a>')
            .data('tag-text', tag.text)
            .data('usl', uslId)
            .appendTo(li);

            ul.append(li);
        }

        return ul;
    }

    function getUSLAutocompleteSource() {
        var uslTexts = [],
            usl;

        for(uslId in usls) {
            usl = usls[uslId];

            uslTexts.push({
                label: usl.ieml_text,
                value: usl.ieml_text
            });

            for(let lang in usl.translations) {
                uslTexts.push({
                    label: usl.translations[lang],
                    value: usl.ieml_text
                });
            }
        }
        return uslTexts;
    }

    function render(tags_, wrapper_, usls_) {
        wrapper = wrapper_ || wrapper;
        tags = tags_ || tags;
        usls = usls_ || usls;

        wrapper.empty();
        wrapper.off('click');
        wrapper.off('submit');

        wrapper.append('<input type="text" class="search" placeholder="Search tag or USL" />');
        var table = $(document.createElement('table'));
        wrapper.append(table);

        var tbody = $('<tbody class="list"></tbody>');
        table.append(tbody);

        var tr, td;
        var tag;

        for(let tagText in tags) {
            tag = tags[tagText];

            tr = $(document.createElement('tr'));

            td = $('<td class="tag">' + tagText + '</td>');
            tr.append(td);

            td = $('<td class="usls" data-tag-text="' + tag.text + '"></td>');
            td.append(buildLinkUSLForm(tag));
            td.append(buildUSLList(tag));
            tr.append(td);

            tbody.append(tr);
        }

        wrapper.on('click', 'td.usls li a', function(e) {
            e.preventDefault();

            var tagText = $(this).data('tag-text'),
                usl = $(this).data('usl');
            var tag = $.extend(true, {}, tags[tagText]);
            signals.unlinkUSL(
                usl, tag,
                updateTag,
                function(msg) {
                    console.log(msg);
                }
            );
        });

        wrapper.on('submit', 'form', function(e) {
            e.preventDefault();
            Tools.cleanFormErrors($(this));
            var _this = this;

            var tagText = $(this).data('tag-text'),
                ieml = $(this).find('.link-usl').val().trim();
            var tag = $.extend(true, {}, tags[tagText]),
                usl = iemlToUSLId(ieml);

            if(!usl) {
                return $(this).find('.field-errors').append(
                    '<div>No such USL: ' + ieml + '</div>'
                );
            }

            signals.linkUSL(
                usl, tag,
                updateTag,
                function(msg) {
                    $(_this).find('.field-errors').append(msg);
                }
            );
        });

        $('td.usls .link-usl').autocomplete({
            source: getUSLAutocompleteSource(),
            minLength: USL_AUTOCOMPLETE_MIN_LEN
        });

        cleanErrors();

        new List(wrapper.attr('id'), LIST_OPTIONS);
    }
    

    function updateUSLList(tag) {
        var ul = buildUSLList(tag);
        $('td[data-tag-text="' + tag.text + '"] ul').replaceWith(ul);
    }

    function error(msg) {
        $(wrapper).find('.error').append('<div>' + msg + '</div>');    
    }

    function cleanErrors() {
        $(wrapper).find('.error').empty();
    }

    return {
        connect: connect,
        error: error,
        render: render
    };
});
