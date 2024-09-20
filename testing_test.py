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

def test_score_of_ten():
    total_score = bowling.score_cruncher("-1 -1 1- 1- -1 -1 1- 1- 1- -1")
    assert total_score == 10

def test_score_of_spare_with_another_frame():
    total_score = bowling.score_cruncher("5/ 1- -- -- -- -- -- -- -- --")
    assert total_score == 12

def test_score_of_three_spares_with_another_frame():
    total_score = bowling.score_cruncher("5/ 1/ 4/ 2- -- -- -- -- -- --")
    assert total_score == 39

def test_score_of_spare_on_last_frame():
    total_score = bowling.score_cruncher("-- -- -- -- -- -- -- -- -- 5/1")
    assert total_score == 12

def test_score_of_double_strike():
    total_score = bowling.score_cruncher("x x -- -- -- -- -- -- -- --")
    assert total_score == 30

def test_score_of_strike_and_two_rolls():
    total_score = bowling.score_cruncher("x 35 -- -- -- -- -- -- -- --")
    assert total_score == 26
