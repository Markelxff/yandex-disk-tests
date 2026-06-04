def test_delete_folder(api, test_folder):
    """Проверяем удаление папки насовсем."""
    response = api.delete_resource(test_folder, permanently=True)
    assert response.status_code in (202, 204)

    get_resp = api.get_resource(test_folder)
    assert get_resp.status_code == 404


def test_delete_folder_to_trash(api, test_folder):
    """Удаление без permanently — папка попадает в корзину."""
    response = api.delete_resource(test_folder, permanently=False)
    assert response.status_code in (202, 204)

    get_resp = api.get_resource(test_folder)
    assert get_resp.status_code == 404


def test_delete_nonexistent_resource(api):
    """Удаление несуществующего ресурса должно вернуть 404."""
    response = api.delete_resource("/nonexistent_xyz_123", permanently=True)
    assert response.status_code == 404