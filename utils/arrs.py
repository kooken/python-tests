def get(array, index, default=None):
    """
    Extracts the value from the list at the specified index, if the index exists.
    If the index does not exist, returns the default value.
    The function only works with non-negative indices.
    :param array: the original list.
    :param index: the index of the element to extract.
    :param default: the default value.
    :return: the value at the index or the default value.
    """

    if 0 <= index < len(array):
        return array[index]
    return default


def my_slice(coll, start=None, end=None):
    """
    Returns a new array containing a copy of a portion of the original array.
    :param coll: the original list.
    :param start: the index at which to begin extracting. If the index is negative,
    start specifies an offset from the end of the list. Defaults to zero.
    :param end: the index at which to end extracting (not including the element at index end).
    If the index is negative, end specifies an offset from the end of the list. Defaults to the length of the original list.
    :return: an array of elements
    """

    length = len(coll)

    if length == 0:
        return []

    if start is None:
        normalized_start = 0
    else:
        normalized_start = start

    if end is None or end > length:
        normalized_end = length
    else:
        normalized_end = end

    return coll[normalized_start:normalized_end]
