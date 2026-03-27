# pytest file should begin with test_
# test should be defined under a function / method
# use of pytest configuration instead of python config

# terminal execution
# cd path to pytest package > py.test -v -s [executes all tests in that package , verbose, -s prints the console]

def test_firstTest(test_fixture):
    print ('Hellow')

def test_secondTest():
    print ('World')

