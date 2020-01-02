"""Pytest fixtures for AuthoritySpoke "Beard Tax Act" examples"""

from typing import Dict, List

import pytest

from authorityspoke.io import loaders, readers

from authorityspoke.codes import Code
from authorityspoke.rules import Rule


@pytest.fixture(scope="module")
def beard_act() -> Dict[str, Code]:
    return loaders.load_and_read_code("beard_tax_act.xml")


@pytest.fixture(scope="class")
def make_beard_rule(beard_act) -> List[Rule]:
    """Rules from the "Beard Tax Act" example statutes."""
    beard_dictionary = loaders.load_holdings("beard_rules.json")
    return readers.read_rules(beard_dictionary, beard_act)
