def test(actual, expected):
    """Compare the actual to the expected value,
        and print a suitable message.
    """
    import sys
    linenum = sys._getframe(1).f_lineno #get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed." .format(linenum)
    else:
        msg = ("Test on line {0} failed. Epected '{1}', but got '{2}'."
                                    .format(linenum, expected, actual))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file)
    """
    test(abs(17), 17)
    test(abs(-17), 17)
    test(abs(0), 0)
    test(abs(3.14), 3.14)
    test(abs(-3.14), 3.14)

test_suite()    # and here is the call to run the tests
