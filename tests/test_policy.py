from src.models import TokenClaims
from src.policy import is_allowed


def test_is_allowed_read_scope():
    claims = TokenClaims(sub="u", scopes=["read"])
    assert is_allowed(claims, "/resources", "GET")


def test_is_forbidden_without_scope():
    claims = TokenClaims(sub="u", scopes=["none"])
    assert not is_allowed(claims, "/resources", "GET")
