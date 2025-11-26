status_code = 200


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == status_code
