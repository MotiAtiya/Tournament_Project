def is_positive_integer_number(n):
    return isinstance(n, int) and not isinstance(n, bool) and n > 0

def is_not_negative_integer_number(n):
    return isinstance(n, int) and not isinstance(n, bool) and n >= 0

def is_non_empty_string(s):
    return len(s) > 0

