def test_create_folder(api, clean_folder_path):
    """Проверяем успешное создание папки."""
    try:
        response = api.create_folder(clean_folder_path)
        assert response.status_code == 201

        info = api.get_resource(clean_folder_path)
        assert info.status_code == 200
    finally:
        api.delete_resource(clean_folder_path, permanently=True)


def test_create_folder_conflict(api, clean_folder_path):
    """Повторное создание той же папки должно вернуть 409 Conflict."""
    api.create_folder(clean_folder_path)
    try:
        response = api.create_folder(clean_folder_path)
        assert response.status_code == 409
    finally:
        api.delete_resource(clean_folder_path, permanently=True)