# fixture usage > more like a prereq for a test method
# parent method that runs before a test method
# pytest.fixture
import pytest

@pytest.mark.usefixtures('test_fixture')
class TestFixture:
    def test_fixtureDemo1(self): #not parameterizing the fixture method because we will just be printing it
        print('execute fixture demo1')

    def test_fixtureDemo2(self):
        print('execute fixture demo2')

    def test_fixtureDemo3(self):
        print('execute fixture demo3')

