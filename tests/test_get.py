from api_client import YandexDiskClient


def test_get_disk_root(api):
    """Проверяем, что можно получить информацию о корне диска."""
    response = api.get_resource("/")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "dir"
    assert "name" in data
    assert "path" in data


def test_get_folder_info(api, test_folder):
    """Проверяем, что можно получить информацию о созданной папке."""
    response = api.get_resource(test_folder)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_folder.lstrip("/")
    assert data["type"] == "dir"


def test_get_nonexistent_resource(api):
    """Запрос несуществующего ресурса должен вернуть 404."""
    response = api.get_resource("/this_path_does_not_exist_xyz_123")
    assert response.status_code == 404


def test_get_resource_unauthorized(base_url):
    """Запрос с невалидным токеном должен вернуть 401."""
    client = YandexDiskClient(base_url, token="invalid_token")
    response = client.get_resource("/")
    assert response.status_code == 401


def test_get_disk_info(api):
    """Проверяем получение общей информации о диске."""
    response = api.get_disk_info()
    assert response.status_code == 200
    data = response.json()
    assert "total_space" in data
    assert "used_space" in data