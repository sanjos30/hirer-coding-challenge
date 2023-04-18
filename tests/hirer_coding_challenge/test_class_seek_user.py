import pytest
from datetime import date

from hirer_coding_challenge.class_seek_user import User
from hirer_coding_challenge.class_user_job import UserJob

@pytest.fixture
def user():
    return User({
        "firstName": "John",
        "lastName": "Doe",
        "jobHistory": [
            {
                "location": "Melbourne",
                "salary": 50000,
                "title": "Software Engineer",
                "fromDate": "2019-01-01",
                "toDate": "2020-06-30"
            },
            {
                "location": "Sydney",
                "salary": 80000,
                "title": "Senior Software Engineer",
                "fromDate": "2020-07-01",
                "toDate": None
            }
        ]
    })

def test_get_average_salary(user):
    assert user.get_average_salary() == 65000

def test_get_current_salary(user):
    assert user.get_current_salary() == 80000

def test_get_current_from_date(user):
    assert user.get_current_from_date() == date.fromisoformat("2020-07-01")

def test_get_current_job(user):
    assert user.get_current_job() == UserJob(
        location="Sydney",
        salary=80000,
        title="Senior Software Engineer",
        from_date=date.fromisoformat("2020-07-01"),
        to_date=None
    )

def test_is_currently_working(user):
    assert user.is_currently_working() == True

def test_get_highest_paying_job(user):
    assert user.get_highest_paying_job() == UserJob(
        location="Sydney",
        salary=80000,
        title="Senior Software Engineer",
        from_date=date.fromisoformat("2020-07-01"),
        to_date=None
    )
