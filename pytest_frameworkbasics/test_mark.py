# pytest file should begin with test_
# test should be defined under a function / method
# use of pytest configuration instead of python config
import pytest


# terminal execution
# cd path to pytest package > py.test -v -s [executes all tests in that package , -v verbose / info , -s prints logs in the console]

# py.test -k second -v -s > -k flag runs only test methods with that keyword in it
# py.test -s -v --html=report.html
# py.test test_mark.py -s -v > will run all the tests only in that file thats passed
# terminal call only tests in this file > py.test filename.py -v -s
# tags /group > mark in pytest > -m flag > py.test -m smoke -v -s
# mark inbuilt marks  > smoke , skip
# xfail > runs the test method but doesnt add it in report because of error

@pytest.mark.smoke
@pytest.mark.skip
def test_firstTest():
    msg = 'Hello'
    assert msg == 'Hi', 'Test failed as the words doesnt match'

@pytest.mark.xfail
def test_secondTest():
    a = 4
    b = 6
    assert a+2 == b, 'a+2 !=b assert fails'














































































































































































































