var USLTagger = (function() {
    var TAG_AUTOCOMPLETE_MIN_LEN = 3;
    var ID = 'usl-tagger';

    var usls, tags = {};

    var listOptions = {
        valueNames: ['usl'] 
    };

    var signals = {};
    function connect(ev, cb) {
        signals[ev] = cb;
    }

    var wrapper = $('<div id="' + ID + '"></div>');
    wrapper.append('<div class="error"></div>');
    wrapper.append('<input type="text" class="search" placeholder="Search USL" />');
    var table = $('<table></table>');
    wrapper.append(table);


    function tagLinked(tag, uslId) {
        tags[tag.text] = $.extend(true, {}, tag);
        $('input.link-tag').autocomplete({
            source: getTagAutocompleteSource(),
            minLength: TAG_AUTOCOMPLETE_MIN_LEN
        });
       updateTagList(usls[uslId]);
    }

    function getTagAutocompleteSource() {
        var texts = [];

        $.each(tags, function(text, tag) {
            texts.push(text);
        });

        return texts;
    }

    function getUSLTags(usl) {
        var selectedTags = new Set([]);

        $.each(tags, function(id, tag) {
            if(tag.usls.indexOf(usl.id) != -1) {
                selectedTags.add(tag);
            }
        });

        return [...selectedTags];
    }

    function getSortedTranslations(translations) {
        var sortable = [];
        for (var lang in translations) {
            sortable.push(lang);
        }
        sortable.sort();
        return sortable;
    }

    // Render

    function updateTagList(usl) {
        $('td.tags[data-uslId="' + usl.id + '"] ul').replaceWith(
            buildTagList(usl)
        );
    }

    function buildUSLColumn(usl) {
        var td = $(document.createElement('td'));
        td.attr('class', 'usl');

        var h3 = $(document.createElement('h3'));
        h3.html(usl.ieml_text);
        td.append(h3);

        for(let lang of getSortedTranslations(usl.translations)) {
            td.append('<div>' + usl.translations[lang] + '</div>');
        }

        return td;
    }

    function buildLinkTagForm(usl) {
        var form = $(document.createElement('form'));
        form.attr('data-uslId', usl.id);

        form.append('<input type="text" class="link-tag" />');
        form.append('<input type="submit" value="Link" />');

        return form;
    }

    function buildTagList(usl) {
        var ul = $(document.createElement('ul'));
        ul.attr('data-uslId', usl.id);
        var tags = getUSLTags(usl);
        var li;

        for(let tag of tags) {
            li = $(document.createElement('li'));
            li.attr('data-tagText', tag.text);
            li.html(tag.text);

            $('<a href="#" class="hide">X</a>')
            .attr('data-tagText', tag.text)
            .attr('data-uslId', usl.id)
            .appendTo(li);

            ul.append(li);
        }

        return ul;
    }

    function buildUSLTagsColumn(usl) {
        var td = $(document.createElement('td'));
        td.attr('class', 'tags');
        td.attr('data-uslId', usl.id);
        td.append(buildLinkTagForm(usl))
        td.append(buildTagList(usl));
        return td;
    }

    function render(usls_, parent_ = null, tags_ = null) {
        usls = usls_ || usls;
        tags = tags_ || tags;

        table.find('tbody').remove();
        var tbody = $('<tbody class="list"></tbody>');
        table.append(tbody);

        var tr;

        $.each(usls, function(id, usl) {
            tr = $(document.createElement('tr'));
            tr.append(buildUSLColumn(usl));
            tr.append(buildUSLTagsColumn(usl));
            tbody.append(tr);
        });

        if(parent_ && !parent_.find('#' + ID).length) {
            parent_.append(wrapper);
            
            table.on('click', 'li a.hide', function(e) {
                e.preventDefault();

                var tagText = $(this).attr('data-tagText'),
                    usl = $(this).attr('data-uslId');
                var tag = $.extend(true, {}, tags[tagText]);

                if(usls[usl] == undefined) {
                    return error('No such USL: ' + usl);
                }

                signals.unlinkTag(tag, usl, tagLinked);
            });

            table.on('submit', 'form', function(e) {
                e.preventDefault();

                var usl = $(this).attr('data-uslId'),
                    tagText = $(this).find('input.link-tag').val().trim(),
                    tag;

                if(!tagText) {
                    return error('The tag cannot be empty.');
                }
                if(tags[tagText] != undefined) {
                    tag = tags[tagText];
                } else {
                    tag = {
                        id: '',
                        usls: [],
                        text: tagText
                    };
                }

                signals.linkTag($.extend(true, {}, tag), usl, tagLinked);
            });

        }

        $('input.link-tag').autocomplete({
            source: getTagAutocompleteSource(),
            minLength: TAG_AUTOCOMPLETE_MIN_LEN
        });

        new List(ID, listOptions);
    }

    function error(err) {
        alert(err);
    }

    return {
        connect: connect,
        error: error,
        render: render
    };
});
