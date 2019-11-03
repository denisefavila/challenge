import random
from loremipsum import generate_paragraph
import pytest

from formater.idwall_formatter import IdwallFormatter

LIMIT = 30


@pytest.fixture
def random_paragraph():
    _, _, paragraph = generate_paragraph()
    return paragraph


def test_formatted_string_without_justify(random_paragraph):
    formatted_string = IdwallFormatter(string=random_paragraph,
                                       limit=LIMIT).format()
    lines = formatted_string.splitlines()
    for line in lines:
        assert len(line) <= LIMIT


def test_formatted_string_with_justify(random_paragraph):
    formatted_string = IdwallFormatter(string=random_paragraph,
                                       limit=LIMIT,
                                       justify=True).format()
    lines = formatted_string.splitlines()

    for i in range(len(lines)):
        assert len(lines[i]) == LIMIT
