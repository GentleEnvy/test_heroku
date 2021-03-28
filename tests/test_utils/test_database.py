from src.utils import database


def test_select():
    assert database.execute(f'SELECT id FROM "user"') == ((1,),)


def test_error():
    database.execute('SELECT * FROM non_existent_table')
