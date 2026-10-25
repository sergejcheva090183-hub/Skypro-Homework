import requests


class YougileApi():
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def create_project(self, name):
        new_project = {"title": name}
        resp = requests.post(
            f"{self.url}/api-v2/projects",
            json=new_project, headers=self.headers
        )

        resp.raise_for_status()
        return resp.json()

    def update_project(self, id: str, new_title: str):
        new_project = {"title": new_title}
        resp = requests.put(
            f"{self.url}/api-v2/projects/{id}",
            json=new_project, headers=self.headers
        )

        resp.raise_for_status()
        return resp.json()

    def get_project(self, project_id):
        resp = requests.get(
            f"{self.url}/api-v2/projects/{project_id}", headers=self.headers
        )

        resp.raise_for_status()
        return resp.json()
