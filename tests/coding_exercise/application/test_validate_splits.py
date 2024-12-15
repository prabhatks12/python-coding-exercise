from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable
import pytest

def test_validate_split_len():
    cables = Splitter().split(Cable(10, "coconuts"), 2)
    valid_split = [3,3,3,1]
    assert len(cables) == len(valid_split)
    assert [cable.length for cable in cables] == valid_split

    cables = Splitter().split(Cable(5, "coconuts"), 2)
    valid_split = [1,1,1,1,1]
    assert len(cables) == len(valid_split)
    assert [cable.length for cable in cables] == valid_split

    cables = Splitter().split(Cable(11, "coconuts"), 3)
    valid_split = [2,2,2,2,2,1]
    assert len(cables) == len(valid_split)
    assert [cable.length for cable in cables] == valid_split


def test_validate_split_names():
    cables = Splitter().split(Cable(10, "coconuts"), 1)
    valid_names = ["coconuts-00", "coconuts-01"]
    assert len(cables) == len(valid_names)
    assert [cable.name for cable in cables] == valid_names


def test_validate_constraints():
    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(100, "coconuts"), 65)

    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(1025, "coconuts"), 32)

    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(1, "coconuts"), 1)

    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(10, "coconuts"), 10)