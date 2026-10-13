import pytest
import requests
from faker import Faker
fake = Faker()


class TestProjectsAPI:

    # Создание проекта(позитивный)
    def test_create_project_positive(self, api_client):
        project_name = f"pos_test_{fake.word()}"
        data = api_client.create_project(name=project_name)

        assert "id" in data
        assert data["id"] is not None and data["id"] != ""

    # Создание проекта с пустым именем (негативный)
    def test_create_project_negative_empty_name(self, api_client):
        with pytest.raises(requests.exceptions.HTTPError):
            api_client.create_project(name="")

    # Получение существующего проекта (позитивный)
    def test_get_project_positive(self, api_client):
        project_name = f"get_test_{fake.word()}"
        create_data = api_client.create_project(name=project_name)
        project_id = create_data["id"]

        data = api_client.get_project(project_id)

        assert data["id"] == project_id
        assert data["title"] == project_name

    # Получение несуществующего проекта (негативный)
    def test_get_project_negative_not_found(self, api_client):

        non_existent_id = 999999999

        with pytest.raises(requests.exceptions.HTTPError):
            api_client.get_project(non_existent_id)

    # Обновление существующего проекта (позитивный)
    def test_update_project_positive(self, api_client):
        project_name = f"upd_test_{fake.word()}"
        new_title = f"updated_{fake.word()}"
        create_data = api_client.create_project(name=project_name)
        project_id = create_data["id"]

        api_client.update_project(project_id, new_title)

        get_data = api_client.get_project(project_id)
        assert get_data["title"] == new_title

    # Обновление несуществующего проекта (негативный)
    def test_update_project_negative_not_found(self, api_client):
        non_existent_id = 999999999

        with pytest.raises(requests.exceptions.HTTPError):
            api_client.update_project(non_existent_id, "some_name")
