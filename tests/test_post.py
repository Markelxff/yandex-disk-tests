import os
import tempfile
import pytest


@pytest.fixture
def sample_file():
    """Создаём временный файл для теста загрузки."""
    content = b"Hello, Yandex.Disk!"
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        file_path = f.name
    yield file_path
    os.unlink(file_path)  # удаляем после теста


def test_upload_file(api, sample_file):
    """Проверяем полный цикл загрузки файла."""
    remote_path = "/test_uploaded_file.txt"

    # 1. Получить ссылку для загрузки
    link_resp = api.get_upload_link(remote_path, overwrite=True)
    assert link_resp.status_code == 200
    upload_url = link_resp.json()["href"]

    # 2. Загрузить файл по ссылке
    upload_resp = api.upload_file(upload_url, sample_file)
    assert upload_resp.status_code == 201

    # 3. Проверить, что файл появился на диске
    info = api.get_resource(remote_path)
    assert info.status_code == 200
    assert info.json()["name"] == "test_uploaded_file.txt"

    # 4. Очистка
    api.delete_resource(remote_path)