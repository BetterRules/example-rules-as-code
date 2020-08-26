"""Pytest fixtures for AuthoritySpoke "Beard Tax Act" examples"""

from typing import Dict, List

import pytest

from legislice.mock_clients import MOCK_BEARD_ACT_CLIENT

from authorityspoke.io import loaders, readers

from authorityspoke.rules import Rule

client = MOCK_BEARD_ACT_CLIENT


@pytest.fixture(scope="function")
def make_beard_rule() -> List[Rule]:
    """Rules from the "Beard Tax Act" example statutes."""
    beard_dictionary = loaders.load_holdings("beard_rules.json")
    return readers.read_holdings(beard_dictionary, client=client)
