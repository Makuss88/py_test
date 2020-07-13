from Student import Student
import pytest


@pytest.fixture(scope='module') # łączymy kilka testów w całość
                                # i w każdym teście dodajemy do nawiasów wynik yielda e.g. "db"
def db():
    print('--start--')
    db = Student()
    db.connect('data.json')
    yield db
    db.close()
    print('---ends---')

# def setup_module(module):
#     global db
#     print('--start--')
#     db = Student()
#     db.connect('data.json')
#
#
# def teardown_module(module):
#     db.close()
#     print('---ends---')


def test_scot_data(db):
    scot_data = db.get_data('Scot')
    assert scot_data['id'] == 1
    assert scot_data['name'] == 'Scot'
    assert scot_data['age'] == 24


def test_mark_data(db):
    scot_data = db.get_data('Mark')
    assert scot_data['id'] == 2
    assert scot_data['name'] == 'Mark'
    assert scot_data['age'] == 36
