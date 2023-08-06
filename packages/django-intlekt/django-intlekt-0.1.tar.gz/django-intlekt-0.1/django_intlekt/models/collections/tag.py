from mongoengine import Document, fields

from .utils import USLField


class Tag(Document):
    """An IEML-translated word used to tag documents."""

    # The meaning can depend on the context, so a tag may have multiple usls.
    # Cannot be empty for the Mongo collection to contain translated tags only.
    # If it could be, there would be two ways to mark a tag as not translated:
    # not in the Mongo collection or with its `usls` attribute empty. It would
    # introduce additional parsing.
    usls = fields.ListField(USLField(required=True,), required=True,)
    text = fields.StringField(unique=True, required=True,)

    meta = {
        'ordering': ['text'],
    }
