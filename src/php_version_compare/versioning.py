from itertools import zip_longest
from typing import List

_SUFFIX_WEIGHT = {
    "dev": 0,
    "alpha": 1,
    "a": 1,
    "beta": 2,
    "b": 2,
    "rc": 3,
    "#": 4,
    "pl": 5,
    "p": 5,
}


def canonicalize_version(version: str) -> str:
    """
    Canonicalize a version string into a "PHP-style" version string. This
    function is used to normalize version strings before comparing them.

    Examples:
        >>> canonicalize_version("1.0")
        '1.0'
        >>> canonicalize_version("1.0-DEV")
        '1.0.DEV'
        >>> canonicalize_version("1.0.1alpha")
        '1.0.1.alpha'
    """

    canonicalized: List[str] = []
    previous_char = None

    for curr_char in version:
        if curr_char in "-+_":
            curr_char = "."
        elif previous_char and (
            (previous_char.isdigit() and curr_char.isalpha())
            or (previous_char.isalpha() and curr_char.isdigit())
        ):
            canonicalized.append(".")

        canonicalized.append(curr_char)
        previous_char = curr_char

    return "".join(canonicalized)


def version_compare(vers1: str, vers2: str) -> int:
    """
    Compare two version strings according to PHP's version_compare function.

    Examples:
        >>> version_compare("1.0", "1.0")
        0
        >>> version_compare("1.0", "1.1")
        -1
        >>> version_compare("1.0-pl1", "1.0")
        1

    Args:
        vers1: The first version string.
        vers2: The second version string.

    Returns:
        -1 if vers1 is less than vers2, 0 if they are equal, 1 if vers1 is
        greater than vers2.
    """

    def _split_version(version: str) -> List[str]:
        return canonicalize_version(version).lower().split(".")

    def _compare_part(part1: str, part2: str) -> int:
        if part1.isdigit() and part2.isdigit():
            return int(part1) - int(part2)
        if part1.isdigit():
            return 1
        if part2.isdigit():
            return -1
        return _SUFFIX_WEIGHT.get(part1, -1) - _SUFFIX_WEIGHT.get(part2, -1)

    vers1_parts = _split_version(vers1)
    vers2_parts = _split_version(vers2)
    for part1, part2 in zip_longest(vers1_parts, vers2_parts, fillvalue="#"):
        result = _compare_part(part1, part2)
        if result != 0:
            return 1 if result > 0 else -1

    return 0
