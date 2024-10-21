import pytest
import json
from signup.schemas import UserSignup

@pytest.fixture
def signup_data():
    with open("__data__/model_data_valid.json", "r") as f:
        data = json.load(f)  # Use json.load to parse the file content to a dict
    return data


@pytest.mark.unit
def test_model_validation(signup_data):
    user_data = UserSignup(**signup_data)
    assert user_data.username == signup_data['username']
    assert user_data is not None