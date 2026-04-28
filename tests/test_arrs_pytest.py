from utils import arrs


def test_get_returns_value_at_index():
    assert arrs.get([1, 2, 3], 1, "default") == 2


def test_get_returns_default_for_empty_list():
    assert arrs.get([], 0, "default") == "default"


def test_get_returns_value_at_first_index():
    assert arrs.get([10, 20, 30], 0, "default") == 10


def test_get_returns_value_at_last_index():
    assert arrs.get([10, 20, 30], 2, "default") == 30


def test_get_returns_default_when_index_out_of_bounds():
    assert arrs.get([1, 2, 3], 5, "default") == "default"


def test_get_returns_default_for_negative_index():
    assert arrs.get([1, 2, 3], -1, "default") == "default"


def test_get_returns_none_as_default():
    assert arrs.get([1, 2, 3], 10) is None


def test_slice_with_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]


def test_slice_with_start_only():
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_slice_with_no_args():
    assert arrs.my_slice([1, 2, 3], None) == [1, 2, 3]


def test_slice_empty_list():
    assert arrs.my_slice([]) == []


def test_slice_with_end_beyond_length():
    assert arrs.my_slice([1, 2, 3], 0, 100) == [1, 2, 3]


def test_slice_with_negative_start():
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]


def test_slice_with_negative_end():
    assert arrs.my_slice([1, 2, 3, 4], 0, -1) == [1, 2, 3]


def test_slice_entire_list():
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
