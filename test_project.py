# test_app.py
import pytest
from unittest.mock import patch, mock_open
from app import get_city, get_category, welcome, goodbye

def test_get_category():
    with patch('builtins.input', side_effect=['2', 'invalid']):
        assert get_category() == 'entertainment'


def test_welcome():
    assert welcome() is True


def test_goodbye():
    assert goodbye() is True
