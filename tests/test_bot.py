import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ai.core import fake_ai
from ai.state import create_default_state


def test_name():
    state = create_default_state()
    r = fake_ai("my name is tu", state)
    assert "tu" in r.lower()


def test_age():
    state = create_default_state()
    fake_ai("i am 30", state)
    r = fake_ai("how old am i", state)
    assert "30" in r


def test_fallback():
    state = create_default_state()
    r = fake_ai("random text", state)
    assert r is not None


def test_context():
    state = create_default_state()
    fake_ai("my name is tu", state)
    fake_ai("i am 30", state)

    r = fake_ai("what about me", state)
    assert "tu" in r.lower()
    assert "30" in r

def test_like_memory():
    state = create_default_state()
    fake_ai("i like coffee", state)

    r = fake_ai("what about me", state)
    assert "coffee" in r.lower()
