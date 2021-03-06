import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from myrats.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HomeController(BaseController):

    def show(self):
        return render('/base/home.mako')

