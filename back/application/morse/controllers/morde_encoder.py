from flask import jsonify, make_response

from back.application.morse.controllers.morse_dictionary import MORSE_DICT
from back.application.morse.schemas import Encoder


class MorseEncoder:
    """MorseEncoder class used to encode a text
    in morse code.

    Attributes:
        _morse_dict (dict): letters of the dictionary and numbers as keys.

    """

    def __init__(self):
        self._morse_dict = MORSE_DICT

    def post(self, request):
        """Method that encodes normal text into morse code.

        Args:
            request (flask request)
        Returns:
            response (:obj: Response): response of the request.

        """
        payload = Encoder().load(request.json)
        text = payload.get("text")
        result = ""
        for i in text.upper():
            if not i in self._morse_dict:
                return make_response(jsonify({"message": "Not a valid caractere"}), 400)
            result += self._morse_dict.get(i) + " "
        return make_response(jsonify({"result": result.rstrip()}), 200)
