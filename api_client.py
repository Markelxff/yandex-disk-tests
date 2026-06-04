import requests


class YandexDiskClient:
    """Клиент для работы с API Яндекс.Диска."""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"OAuth {token}"}

    def get_disk_info(self):
        """GET — получить общую информацию о диске."""
        return requests.get(self.base_url, headers=self.headers)

    def get_resource(self, path, params=None):
        """GET — получить информацию о файле или папке."""
        url = f"{self.base_url}/resources"
        p = {"path": path}
        if params:
            p.update(params)
        return requests.get(url, headers=self.headers, params=p)

    def create_folder(self, path):
        """PUT — создать папку."""
        url = f"{self.base_url}/resources"
        params = {"path": path}
        return requests.put(url, headers=self.headers, params=params)

    def get_upload_link(self, path, overwrite=False):
        """GET — получить ссылку для загрузки файла (шаг 1 для POST)."""
        url = f"{self.base_url}/resources/upload"
        params = {"path": path, "overwrite": str(overwrite).lower()}
        return requests.get(url, headers=self.headers, params=params)

    def upload_file(self, upload_url, file_path):
        """PUT — загрузить файл по полученной ссылке (шаг 2 для POST)."""
        with open(file_path, "rb") as f:
            return requests.put(upload_url, data=f)

    def delete_resource(self, path, permanently=False):
        """DELETE — удалить файл или папку."""
        url = f"{self.base_url}/resources"
        params = {"path": path, "permanently": str(permanently).lower()}
        return requests.delete(url, headers=self.headers, params=params)