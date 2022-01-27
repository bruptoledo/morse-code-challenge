def test_post_morse_encoder(client):
    request = client.post(
        path="morse/encode",
        json={"text": "a"},
    )

    assert request.status_code == 200
    response = request.json
    assert response["result"] == ".-"


def test_post_morse_encoder_complete(client):
    request = client.post(
        path="morse/encode",
        json={"text": "abcdefghijklmnopqrstuvwxyz1234567890 "},
    )

    assert request.status_code == 200
    response = request.json
    assert (
        response["result"]
        == ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
    )


def test_post_morse_invalid_character(client):
    request = client.post(
        path="morse/encode",
        json={"text": "*"},
    )
    assert request.status_code == 400
    response = request.json
    assert response["message"] == "Not a valid caractere"
