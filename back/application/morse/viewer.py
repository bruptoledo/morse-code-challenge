from flask import request
from flask_accepts import accepts
from flask_restplus import Resource, Namespace

from back.app import api
from back.application.morse.controllers import MorseDecoder, MorseEncoder
from back.application.morse.schemas import Decoder, Encoder

morse_ns = Namespace("morse", description="Provide a way to encode and decode texts in morse code.")


@morse_ns.route("/decode", methods=["POST"])
class MorseDecoderViewer(Resource):
    @accepts(schema=Decoder, api=api)
    def post(self):
        morse_decoder = MorseDecoder()
        return morse_decoder.post(request)


@morse_ns.route("/encode", methods=["POST"])
class MorseEncoderViewer(Resource):
    @accepts(schema=Encoder, api=api)
    def post(self):
        morse_encoder = MorseEncoder()
        return morse_encoder.post(request)
