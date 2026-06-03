def test_delete_folder(api, test_folder):
    """Проверяем удаление папки."""
    # Создаём папку
    api.create_folder(test_folder)

    # Удаляем
    response = api.delete_resource(test_folder)
    assert response.status_code in [200, 202, 204]

    # Проверяем, что папки больше нет
    get_resp = api.get_resource(test_folder)
    assert get_resp.status_code == 404