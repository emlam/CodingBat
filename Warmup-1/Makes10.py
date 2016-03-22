def makes10(a, b):
    """
    Given 2 ints, a and b,
    return True if one if them
    is 10 or if their sum is 10.
    """

    if a + b == 10:
        print True
    elif a == 10 or b ==10:
        print True
    else:
        print False

makes10(8, 3)
