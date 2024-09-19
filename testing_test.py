import pytest
import bowling

def test_all_gutter_balls():
    total_score = bowling.score_cruncher("-- -- -- -- -- -- -- -- -- --")
    assert total_score == 0


def test_score_of_one_should_return_one():
    total_score = bowling.score_cruncher("-1 -- -- -- -- -- -- -- -- --")
    assert total_score == 1

def test_score_of_single_strike():
    total_score = bowling.score_cruncher("x -- -- -- -- -- -- -- -- --")
    assert total_score == 10

def test_score_of_spare():
    total_score = bowling.score_cruncher("5/ -- -- -- -- -- -- -- -- --")
    assert total_score == 10