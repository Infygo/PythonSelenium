# use of a common initialization method to be reused by different test methods in different files
# use of conftest file > common file for initialization methods for different test methods across different files
# cant pass the fixture name from conftest file for all methods in a class file > use it at top of the class level using annotations
# this will ensure fixtures are applied to all methods in that class
# use of fixture at scope class level @pytest.fixture(scope="class")> runs once at class level > Before methods and after methods in the class

# datadriven parameterization - use of fixtures to pass multiple datasets to the tests - dataset parameterization


import pytest


@pytest.fixture(scope="class")
def test_fixture():
    print('Executing 1st step from fixture ')
    yield
    print('Executing as last step from fixture ')

@pytest.fixture
def test_fixturedata():
    user_dictionary = {'userFname': 'vignesh', 'userLname': 'rav', 'email': 'vig89@gmail.com'}
    return user_dictionary

@pytest.fixture(params=[("chrome", "vignesh"), ("firefox","vignesh"),("IE","vignesh")])
def test_crossbrowser(request):
    return request.param
