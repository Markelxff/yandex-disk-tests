def test_get_disk_root(api):
    """Проверяем, что можно получить информацию о корне диска."""
    response = api.get_resource("/")
    assert response.status_code == 200
    data = response.json()
    assert "type" in data
    assert data["type"] == "dir"


def test_get_folder_info(api, test_folder):
    """Проверяем, что можно получить информацию о созданной папке."""
    # Создаём папку
    api.create_folder(test_folder)

    # Получаем информацию
    response = api.get_resource(test_folder)
    assert response.status_code == 200
    assert response.json()["name"] == test_folder.lstrip("/")

    # Очистка
    api.delete_resource(test_folder)