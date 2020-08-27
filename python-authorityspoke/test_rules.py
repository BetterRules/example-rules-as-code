"""
Tests from the statute_rules Jupyter Notebook.

Please check statute_rules.ipynb for explanations.
"""

import pytest

from legislice.mock_clients import MOCK_BEARD_ACT_CLIENT

from authorityspoke.facts import Fact
from authorityspoke.entities import Entity
from authorityspoke.predicates import Predicate, Q_
from authorityspoke.procedures import Procedure
from authorityspoke.rules import Rule

from authorityspoke.io import loaders, readers

client = MOCK_BEARD_ACT_CLIENT


class TestStatuteRules:
    """
    Tests from the statute_rules Jupyter Notebook.
    """

    def test_greater_than_implies_equal(self, make_beard_rule):
        beard_dictionary = loaders.load_holdings("beard_rules.json")
        beard_dictionary[0]["inputs"][1][
            "content"
        ] = "the length of the suspected beard was = 8 millimetres"
        longer_hair_rule = readers.read_rule(beard_dictionary[0], client=client)
        assert make_beard_rule[0].implies(longer_hair_rule)

    def test_greater_than_contradicts_not_greater(self, make_beard_rule):
        beard_dictionary = loaders.load_holdings("beard_rules.json")
        beard_dictionary[1]["inputs"][1][
            "content"
        ] = "the length of the suspected beard was >= 12 inches"
        beard_dictionary[1]["outputs"][0]["truth"] = False
        beard_dictionary[1]["mandatory"] = True
        long_hair_is_not_a_beard = readers.read_rule(beard_dictionary[1], client=client)
        assert make_beard_rule[1].contradicts(long_hair_is_not_a_beard)

    def test_contradictory_fact_about_beard_length(self, make_beard_rule):
        beard_dictionary = loaders.load_holdings("beard_rules.json")
        beard_dictionary[1]["despite"] = beard_dictionary[1]["inputs"][0]
        beard_dictionary[1]["inputs"] = {
            "type": "fact",
            "content": "the length of the suspected beard was >= 12 inches",
        }
        beard_dictionary[1]["outputs"][0]["truth"] = False
        beard_dictionary[1]["mandatory"] = True
        long_thing_is_not_a_beard = readers.read_rule(
            beard_dictionary[1], client=client
        )
        assert make_beard_rule[1].contradicts(long_thing_is_not_a_beard)

    def test_contradictory_fact_about_beard_length_reverse(
        self, make_beard_rule,
    ):
        beard_dictionary = loaders.load_holdings("beard_rules.json")
        beard_dictionary[1]["despite"] = beard_dictionary[1]["inputs"][0]
        beard_dictionary[1]["inputs"] = {
            "type": "fact",
            "content": "the length of the suspected beard was >= 12 inches",
        }
        beard_dictionary[1]["outputs"][0]["truth"] = False
        beard_dictionary[1]["mandatory"] = True
        long_thing_is_not_a_beard = readers.read_rule(
            beard_dictionary[1], client=client
        )
        assert long_thing_is_not_a_beard.contradicts(make_beard_rule[1])

    @pytest.mark.parametrize(
        (
            "facial_hair_over_5mm, facial_hair_on_or_below_chin, "
            "facial_hair_uninterrupted, outcome"
        ),
        (
            [False, False, True, False],
            [False, False, False, False],
            [False, True, False, False],
            [False, True, True, False],
            [True, False, True, True],
            [True, False, False, False],
            [True, True, True, True],
            [True, True, None, True],
            [True, None, True, True],
        ),
    )
    def test_is_beard_implied(
        self,
        facial_hair_over_5mm,
        facial_hair_on_or_below_chin,
        facial_hair_uninterrupted,
        outcome,
        make_beard_rule,
    ):
        beard = Entity("a facial feature")

        sec_4 = client.read(path="/test/acts/47/4/")

        hypothetical = Rule(
            procedure=Procedure(
                inputs=[
                    Fact(Predicate("{} was facial hair"), context_factors=beard),
                    Fact(
                        Predicate(
                            "the length of {} was {}",
                            comparison=">=",
                            quantity=Q_("5 millimeters"),
                            truth=facial_hair_over_5mm,
                        ),
                        context_factors=beard,
                    ),
                    Fact(
                        Predicate(
                            "{} occurred on or below the chin",
                            truth=facial_hair_on_or_below_chin,
                        ),
                        context_factors=beard,
                    ),
                    Fact(
                        Predicate(
                            "{} existed in an uninterrupted line from the front "
                            "of one ear to the front of the other ear below the nose",
                            truth=facial_hair_uninterrupted,
                        ),
                        context_factors=beard,
                    ),
                ],
                outputs=Fact(Predicate("{} was a beard"), context_factors=beard),
            ),
            enactments=sec_4,
        )

        meets_chin_test = make_beard_rule[0].implies(hypothetical)
        meets_ear_test = make_beard_rule[1].implies(hypothetical)
        assert outcome == meets_chin_test or meets_ear_test

    def test_adding_definition_of_transfer(self, make_beard_rule):
        loan_is_transfer = make_beard_rule[7]
        elements_of_offense = make_beard_rule[11]
        loan_without_exceptions = (
            loan_is_transfer
            + elements_of_offense.inputs[1]
            + elements_of_offense.inputs[2]
            + elements_of_offense.enactments[1]
        )
        combined = loan_without_exceptions + elements_of_offense
        assert combined
