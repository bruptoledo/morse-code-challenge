from marshmallow import fields, Schema


class Decoder(Schema):
    text = fields.String(required=True)
