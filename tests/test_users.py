def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_user(api_client):
    data = {
        "name": "Thiago Silva",
        "email": "thiago@test.com"
    }

    response = api_client.post("/users", data)

    assert response.status_code == 201
    assert response.json()["name"] == "Thiago Silva"


def test_update_user(api_client):
    data = {
        "name": "Updated User"
    }

    response = api_client.put("/users/1", data)

    assert response.status_code == 200


def test_delete_user(api_client):
    response = api_client.delete("/users/1")

    assert response.status_code == 200
