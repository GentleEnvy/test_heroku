import re

from tests.conftest import parameterize
from src.utils.functions import generate_random_token


@parameterize('length', (30, 50, 100))
def test_generate_random_token(length):
    assert re.match(
        f'.{{{length}}}',
        generate_random_token(length)
    )
