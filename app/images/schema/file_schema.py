import mongoengine as me

class File(me.Document):
    path=me.StringField(required=True)
    createdAt=me.IntField()
    filename=me.StringField()
    size=me.IntField()