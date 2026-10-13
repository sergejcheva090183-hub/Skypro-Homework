import os
import pytest
from dotenv import load_dotenv
from lesson_08.api_yougile import YougileApi

load_dotenv()


@pytest.fixture
def api_client():

    return YougileApi(
        url=os.environ.get("YOUGILE_URL", "https://your.yougile.com"),
        token=os.environ["YOUGILE_TOKEN"]
    )
