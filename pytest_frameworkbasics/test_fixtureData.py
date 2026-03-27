import pytest


#@pytest.mark.usefixtures("test_fixturedata")
class Testfixturedataload:
    def test_editprofile(self,test_fixturedata):  # parameterizing the fixture because we will be using data from that fixture method
        print("Editing user profile")
        for i in test_fixturedata:
            print(test_fixturedata[i])
    def test_browser(self, test_crossbrowser):
        print("Data parameterization:" , test_crossbrowser)
        print('browservalues:', test_crossbrowser[0])
