var Tools = {};

Tools.documentToStr = function(document_) {
    if (!document_.title) {
        return document_.url;
    }

    return document_.title;
};

Tools.getPostTitle = function(post, documents) {
    var document_ = documents[post.document];

    if(document_ === undefined) {
        throw 'Unknown document ' + post.document;
    }

    return Tools.documentToStr(document_);
};

Tools.getUnlinkedDocuments = function(collection, documents) {
    var unlinkedDocuments = $.extend(true, {}, documents);

    for(let document_ in collection.posts) {
        delete unlinkedDocuments[document_];
    }

    return unlinkedDocuments;
};

Tools.FIELD_ERRORS_HTML = '<div class="field-errors"></div>';

Tools.renderFormErrors = function(form, errors) {
    for(let field in errors) {
        form.find('*[name="' + field + '"]')
        .next('div.field-errors')
        .html(errors[field]);
    }
};

Tools.cleanFormErrors = function(form) {
    form.find('.field-errors').html('');
};

Tools.cleanFormFields = function(form) {
    form.find(':not(*[type="hidden"], *[type="submit"])').val('');
    form.find('textarea').val('');
};

Tools.fillForm = function(object, form) {
    for(let key in object) {
        form.find('*[name="' + key + '"]').val(object[key]);
    }
};

Tools.commaStrToArray = function(str) {
    var array = str.split(',').map(function(s) { return s.trim(); });
    // If str is an empty string, array == [''], but we want []
    return !array[0] ? [] : array;
};

Tools.listToCommaStr = function(list) {
    return list.join(', ');
};

Tools.getCollectionTextTags = function(collection) {
    var tags = new Set([]);

    $.each(collection.posts, function(id, post) {
        for(let tag of post.tags) {
            tags.add(tag);
        }
    });

    return [...tags];
};
    
Tools.createTag = function(text) {
    return {
        text: text,
        id: '',
        usls: []
    };
};
