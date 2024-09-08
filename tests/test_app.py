from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/create_user/',
        json={'name': 'Vitor', 'cpf': 43806399085, 'birth_date': '2000-03-14'},
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'Vitor',
        'birth_date': '2000-03-14',
    }


def test_read_user(client):
    response = client.get('/read_user/1')

    response.status_code == HTTPStatus.OK
    response.json() == {
        'id': 1,
        'name': 'Vitor',
        'birth_date': '2000-03-14',
    }


def test_error_read_user(client):
    response = client.get(
        '/read_user/999',
    )

    response.status_code == HTTPStatus.NOT_FOUND
    response.json() == {'detail': 'User not found'}


def test_read_users(client):
    response = client.get('/read_users/')

    response.status_code == HTTPStatus.OK
    response.json() == {
        'id': 1,
        'name': 'Vitor',
        'birth_date': '2000-03-14',
    }
