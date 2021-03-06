def test_post_morse_decoder(client):
    request = client.post(
        path="morse/decode",
        json={"text": ".-"},
    )

    assert request.status_code == 200
    response = request.json
    assert response["result"] == "A"


def test_post_morse_decoder_complete(client):
    request = client.post(
        path="morse/decode",
        json={
            "text": ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        },
    )

    assert request.status_code == 200
    response = request.json
    assert response["result"] == "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def test_post_morse_decoder_invalid_character(client):
    request = client.post(
        path="morse/decode",
        json={"text": ".-*"},
    )

    assert request.status_code == 400
    response = request.json
    assert response["message"] == "Not a valid morse code"


def test_post_morse_decoder_invalid_payload(client):
    request = client.post(
        path="morse/decode",
        json={},
    )

    assert request.status_code == 400
    response = request.json
    assert response["schema_errors"]["text"][0] == "Missing data for required field."


def test_post_morse_decoder_unknown_field(client):
    request = client.post(
        path="morse/decode",
        json={"text": ".-*", "a": "a"},
    )

    assert request.status_code == 400
    response = request.json
    assert response["schema_errors"]["a"][0] == "Unknown field."
