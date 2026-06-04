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
    os.unlink(file_path)


@pytest.fixture
def remote_test_file(api):
    """Фикстура для удалённого файла — гарантированно удаляет после теста."""
    path = "/test_uploaded_file.txt"
    yield path
    api.delete_resource(path, permanently=True)


def test_upload_file(api, sample_file, remote_test_file):
    """Проверяем полный цикл загрузки файла."""
    # 1. Получить ссылку для загрузки
    link_resp = api.get_upload_link(remote_test_file, overwrite=True)
    assert link_resp.status_code == 200
    upload_url = link_resp.json()["href"]

    # 2. Загрузить файл по ссылке
    upload_resp = api.upload_file(upload_url, sample_file)
    assert upload_resp.status_code == 201

    # 3. Проверить, что файл появился на диске
    info = api.get_resource(remote_test_file)
    assert info.status_code == 200
    assert info.json()["name"] == "test_uploaded_file.txt"
    assert info.json()["type"] == "file"