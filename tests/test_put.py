def test_create_folder(api, test_folder):
    """Проверяем успешное создание папки."""
    response = api.create_folder(test_folder)
    assert response.status_code == 201

    # Убедимся, что папка действительно существует
    info = api.get_resource(test_folder)
    assert info.status_code == 200

    # Очистка
    api.delete_resource(test_folder)


def test_create_folder_conflict(api, test_folder):
    """Повторное создание той же папки должно вернуть 409 Conflict."""
    # Создаём папку первый раз
    api.create_folder(test_folder)

    # Пробуем создать ещё раз
    response = api.create_folder(test_folder)
    assert response.status_code == 409

    # Очистка
    api.delete_resource(test_folder)