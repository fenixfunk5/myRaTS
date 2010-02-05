from myrats.tests import *

class TestTicketController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='ticket', action='index'))
        # Test response...
