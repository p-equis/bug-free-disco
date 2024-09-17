import pytest
import bowling

def test_pytest_is_working():
    total_score = bowling.score_cruncher([0, 0, 0])
    assert total_score == 0
