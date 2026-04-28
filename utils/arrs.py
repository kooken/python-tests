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
    Returns a new list containing a copy of a portion of the original list.
    :param coll: the original list.
    :param start: the index at which to begin extracting. If negative, specifies
    an offset from the end of the list. Defaults to zero.
    :param end: the index at which to stop extracting (exclusive). If negative,
    specifies an offset from the end of the list. Defaults to the length of the list.
    :return: a new list of the extracted elements.
    """
    return coll[start:end]
