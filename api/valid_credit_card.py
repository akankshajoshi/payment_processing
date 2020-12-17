import re

PATTERN = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'


def is_valid(sequence):
    """Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6
    - must only consist of digits (0-9) or hyphens '-',
    - may have digits in groups of 4, separated by one hyphen "-".
    - must NOT use any other separator like ' ' , '_',
    - must NOT have 4 or more consecutive repeated digits.
    """
    # import pdb;pdb.set_trace()
    match = re.match(PATTERN, sequence)

    if not match:
        return False

    for group in match.groups():
        if group[0] * 4 == group:
            return False
    return True

