![Tests](https://github.com/Markelxff/yandex-disk-tests/actions/workflows/tests.yml/badge.svg)
# Автотесты для API Яндекс.Диска

Проект с автотестами для проверки REST API Яндекс.Диска.

## Стек
- Python 3
- pytest
- requests

## Тестируемые методы
- GET — получение информации о ресурсе
- PUT — создание папки
- POST — загрузка файла
- DELETE — удаление ресурса

## Как запустить

### 1. Получить токен
Перейди на Полигон Яндекс.Диска:
https://yandex.ru/dev/disk/poligon/

Нажми «Получить токен» и скопируй его.

### 2. Создать .env файл
Скопируй `.env.example` в `.env` и вставь свой токен:


### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Запустить тесты
```bash
pytest
```
