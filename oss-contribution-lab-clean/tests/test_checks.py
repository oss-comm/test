import pytest

from oss_repo_check.checks import parse_repo


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("pallets/flask", ("pallets", "flask")),
        ("https://github.com/pallets/flask", ("pallets", "flask")),
        ("https://github.com/pallets/flask/", ("pallets", "flask")),
    ],
)
def test_parse_repo(value, expected):
    assert parse_repo(value) == expected


@pytest.mark.parametrize("value", ["flask", "a/b/c", "", "https://example.com/a/b"])
def test_parse_repo_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        parse_repo(value)
