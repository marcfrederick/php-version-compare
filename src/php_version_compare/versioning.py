import sys
from itertools import zip_longest
from typing import Iterable, Optional, Union, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

Operator = Literal[
    "<", "lt", "<=", "le", ">", "gt", ">=", "ge", "==", "=", "eq", "!=", "<>", "ne"
]

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


def _split_version(version: str) -> Iterable[str]:
    """
     Split a version string into its components. This function is used to split a
     version string into its major, minor, patch, and suffix components.

    Examples:
         >>> list(_split_version("1.0"))
         ['1', '0']
         >>> list(_split_version("1.0-DEV"))
         ['1', '0', 'DEV']
         >>> list(_split_version("1.0.1alpha"))
         ['1', '0', '1', 'alpha']

     Args:
         version: The version string to split.

     Yields:
         The components of the version string.
    """
    current_segment = ''

    for curr_char in version:
        if curr_char in "-+_.":
            yield current_segment
            current_segment = ''
        elif current_segment and (
            (current_segment[-1].isdigit() and curr_char.isalpha())
            or (current_segment[-1].isalpha() and curr_char.isdigit())
        ):
            yield current_segment
            current_segment = curr_char
        else:
            current_segment += curr_char

    yield current_segment


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

    Args:
        version: The version string to canonicalize.

    Returns:
        The canonicalized version string.
    """
    return ".".join(_split_version(version))


def _version_compare(version1: str, version2: str) -> int:
    def _compare_part(part1: str, part2: str) -> int:
        if part1.isdigit() and part2.isdigit():
            return int(part1) - int(part2)
        if part1.isdigit():
            return 1
        if part2.isdigit():
            return -1
        return _SUFFIX_WEIGHT.get(part1, -1) - _SUFFIX_WEIGHT.get(part2, -1)

    version1_parts = [part.lower() for part in _split_version(version1)]
    version2_parts = [part.lower() for part in _split_version(version2)]
    for part1, part2 in zip_longest(version1_parts, version2_parts, fillvalue="#"):
        result = _compare_part(part1, part2)
        if result != 0:
            return 1 if result > 0 else -1

    return 0


@overload
def version_compare(version1: str, version2: str) -> int: ...


@overload
def version_compare(version1: str, version2: str, operator: Operator) -> bool: ...


def version_compare(
    version1: str, version2: str, operator: Optional[Operator] = None
) -> Union[int, bool]:
    """
    Compare two version strings according to PHP's version_compare function.

    Examples:
        >>> version_compare("1.0", "1.0")
        0
        >>> version_compare("1.0", "1.1")
        -1
        >>> version_compare("1.0-pl1", "1.0")
        1
        >>> version_compare("1.0", "1.0", "==")
        True
        >>> version_compare("1.0", "1.1", "<")
        True
        >>> version_compare("1.0", "1.1", ">")
        False

    Args:
        version1: The first version string.
        version2: The second version string.
        operator: The (optional) comparison operator. Must be one of "<", "lt", "<=",
            "le", ">", "gt", ">=", "ge", "==", "=", "eq", "!=", "<>", or "ne".

    Returns:
        If `operator` is None, returns -1 if `version1` is less than `version2`, 0 if
        they are equal, and 1 if `version1` is greater than `version2`. If `operator` is
        provided, returns True if the comparison is true, and False otherwise.
    """
    result = _version_compare(version1, version2)
    if operator is None:
        return result
    elif operator in ("<", "lt"):
        return result < 0
    elif operator in ("<=", "le"):
        return result <= 0
    elif operator in (">", "gt"):
        return result > 0
    elif operator in (">=", "ge"):
        return result >= 0
    elif operator in ("==", "=", "eq"):
        return result == 0
    elif operator in ("!=", "<>", "ne"):
        return result != 0
    else:
        raise ValueError(f"Invalid operator: {operator}")
