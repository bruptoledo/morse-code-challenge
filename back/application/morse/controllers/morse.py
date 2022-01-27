from werkzeug.exceptions import NotImplemented


class Morse:
    """Morse parent class for inheriting the MorseEncoder and MorseDecoder classes.

    Attributes:
        _morse_dict (dict): letters of the dictionary and numbers as keys.
        _morse_dict_reversed (dict): morse code as keys.

    Raises:
        NotImplemented: If post function is called without implementation.

    """

    def __init__(self):
        self._morse_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            " ": " ",
        }
        self._morse_dict_reversed = {value: key for key, value in self._morse_dict.items()}

    def post(self, request):
        raise NotImplemented
