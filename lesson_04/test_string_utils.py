import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("skypro", "Skypro"),
        ("SKYPRO", "Skypro"),
        ("123abc", "123abc"),
        ("", ""),
        (" hello", " hello"),
    ]
)
def test_capitalize(utils, input_text, expected):
    assert utils.capitalize(input_text) == expected

@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   test", "test"),
        (" test", "test"),
        ("test", "test"),
        ("     ", ""),
        ("", ""),
    ],
)
def test_trim_edge_cases(utils, input_str, expected):
    assert utils.trim(input_str) == expected

def test_trim_type_error(utils):
    with pytest.raises(AttributeError):
        utils.trim(None)

@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False),
        ("SkyPro", "Pro", True),
        ("", "a", False),
        ("abc", "", True),
        ("aaaa", "aa", True),
    ],
)
def test_contains_various(utils, string, symbol, expected):
    assert utils.contains(string, symbol) is expected

def test_contains_case_sensitive(utils):
    assert utils.contains("SkyPro", "s") is False

def test_contains_type_error(utils):
    with pytest.raises(AttributeError):
        utils.contains(123, "1")

@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("banana", "na", "ba"),
        ("testtest", "test", ""),
        ("", "x", ""),
        ("aaa", "a", ""),
        ("sp ace", " ", "space"),
    ],
)
def test_delete_symbol_various(utils, string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected

def test_delete_symbol_empty_pattern(utils):
    assert utils.delete_symbol("data", "") == "data"

def test_delete_symbol_type_error(utils):
    with pytest.raises(TypeError):
        utils.delete_symbol("text", None)
