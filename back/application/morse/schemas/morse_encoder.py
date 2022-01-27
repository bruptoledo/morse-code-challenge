from marshmallow import fields, Schema


class Encoder(Schema):
    text = fields.String(required=True)
