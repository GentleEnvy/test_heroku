import os

from testfixtures import TempDirectory
import pytest
from pytest import fixture

__import__('src.main')

parameterize = pytest.mark.parametrize


@fixture()
def temp_dir():
    with TempDirectory() as temp_directory:
        yield temp_directory


@fixture()
def temp_text_file(temp_dir):
    with open(os.path.join(temp_dir.path, 'temp_text_file.txt'), 'w+') as temp_file:
        yield temp_file


@fixture()
def test_image():
    with open(os.getcwd() + '/tests/test_utils/test_image.jpg', 'rb') as test_image_:
        yield test_image_
