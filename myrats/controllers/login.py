import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from myrats.lib.base import BaseController, render

log = logging.getLogger(__name__)

class LoginController(BaseController):

    def index(self):
        # Return a rendered template
        return render('/component/login.mako')
        # or, return a response
        #return 'Hello World'
        
    def private(self):
        response.status = "401 Not authenticated"
        return "You are not authenticated"

