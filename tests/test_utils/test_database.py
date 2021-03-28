from src.utils import database


def test_select():
    assert database.execute('SELECT id FROM "user"') == ((1,),)
