from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable
import pytest

def test_validate_split_len():
    """
    Validating the splits length
    """
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
    """
    Validating the new splits name
    """
    cables = Splitter().split(Cable(10, "coconuts"), 1)
    assert [cable.name for cable in cables] == ["coconuts-0"+str(i) for i in range(2)]

    cables = Splitter().split(Cable(11, "coconuts"), 3)
    assert [cable.name for cable in cables] == ["coconuts-0"+str(i) for i in range(6)]


def test_validate_constraints():
    """
    Validating the constraints which will throw ValueError
    """
    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(100, "coconuts"), 65)

    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(1025, "coconuts"), 32)

    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(1, "coconuts"), 1)

    with pytest.raises(ValueError):
        cables = Splitter().split(Cable(10, "coconuts"), 10)