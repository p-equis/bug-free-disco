import pytest
import bowling

def test_all_gutter_balls():
    total_score = bowling.score_cruncher("-- -- -- -- -- -- -- -- -- --")
    assert total_score == 0


def test_score_of_one_should_return_one():
    total_score = bowling.score_cruncher("-1 -- -- -- -- -- -- -- -- --")
    assert total_score == 1
