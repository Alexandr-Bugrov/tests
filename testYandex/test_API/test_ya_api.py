import pytest
from main import YaUploader

YaTest = YaUploader('')


@pytest.mark.parametrize('code', [201, 409])
def test_create_folder(code):
    assert YaTest.create_folder('my_folder').status_code == code
