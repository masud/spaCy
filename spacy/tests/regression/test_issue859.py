# encoding: utf8
from __future__ import unicode_literals

import pytest


@pytest.mark.xfail
@pytest.mark.parametrize('text', ["aaabbb@ccc.com\nThank you!"])
def test_issue859(en_tokenizer, text):
    """Test that no extra space is added in doc.text method."""
    doc = en_tokenizer(text)
    assert ' ' not in doc.text
    assert doc.text == text
