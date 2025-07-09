import pytest
from geometry import Square, Circle, area_stats

def test_square_area_zero_and_positive():
# Arrange: choose side lengths
    s = Square(5)
# Act: compute areas
    ans = 25
# Assert: use pytest.approx to compare with expected
    assert pytest.approx(s.area()) == pytest.approx(ans)


def test_stats_keys_and_values():
    # Arrange: create several shapes
    s = Square(10) #100
    c = Circle(4) #50.27
    s2 = Square(42) #1764
    c2 = Circle(33) #3421.19
    shapes = [s, c, s2, c2]
    # Act: call area_stats

    d = area_stats(shapes)

    # Assert: stats is dict, has correct keys, and values are numbers
    assert isinstance(d, dict)
    assert "n" in d
    assert "total" in d
    assert "mean" in d
    assert "min" in d
    assert "max" in d
    assert all(isinstance(value, (int, float)) for value in d.values())

    assert d["n"] == 4

    #Rounded to account for extra decimals from pi
    assert round(d["total"], 2) == 5335.46
    assert round(d["mean"], 3) == 1333.865
    assert round(d["min"], 2) == 50.27
    assert round(d["max"], 2) == 3421.19

def test_stats_raises_without_shapes():
    shapes = []
    with pytest.raises(ValueError):
        area_stats(shapes)