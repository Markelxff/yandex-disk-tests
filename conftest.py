import os
import pytest
from dotenv import load_dotenv
from api_client import YandexDiskClient

load_dotenv()


@pytest.fixture(scope="session")
def token():
    """Получаем токен из переменной окружения."""
    t = os.getenv("YANDEX_DISK_TOKEN")
    if not t:
        raise RuntimeError(
            "Не задан YANDEX_DISK_TOKEN. "
            "Получи токен в Полигоне: https://yandex.ru/dev/disk/poligon/"
        )
    return t


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API Яндекс.Диска."""
    return "https://cloud-api.yandex.net/v1/disk"


@pytest.fixture
def api(token, base_url):
    """Готовый клиент API для использования в тестах."""
    return YandexDiskClient(base_url, token)


@pytest.fixture
def test_folder():
    """Путь к тестовой папке — общий для всех тестов."""
    return "/test_api_folder"