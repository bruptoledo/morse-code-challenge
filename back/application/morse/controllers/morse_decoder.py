from flask import jsonify, make_response

from back.application.morse.controllers.morse import Morse


class MorseDecoder(Morse):
    """MorseDecoder class used to decode a text in morse code.

    Attributes:
        _morse_dict (dict): letters of the dictionary and numbers as keys.
        _morse_dict_reversed (dict): morse code as keys.

    """

    def post(self, request):
        """Method that decodes morse code into normal text.

        Args:
            request (flask request)
        Returns:
            response (:obj: Response): response of the request.

        """
        payload = request.json
        text = payload.get("text")
        result = ""
        for i in text.split():
            if not i in self._morse_dict_reversed:
                return make_response(jsonify({"message": "Not a valid morse code"}), 400)
            result += self._morse_dict_reversed.get(i)
        return make_response(jsonify({"result": result}), 200)
