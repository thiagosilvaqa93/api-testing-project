from utils.api_client import APIClient

api = APIClient()


def test_get_users():
    response = api.get("/users")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_user():
    data = {
        "name": "Thiago Silva",
        "email": "thiago@test.com"
    }

    response = api.post("/users", data)

    assert response.status_code == 201
    assert response.json()["name"] == "Thiago Silva"


def test_update_user():
    data = {
        "name": "Updated User"
    }

    response = api.put("/users/1", data)

    assert response.status_code == 200


def test_delete_user():
    response = api.delete("/users/1")

    assert response.status_code == 200