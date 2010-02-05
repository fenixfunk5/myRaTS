from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1265296431.785085
_template_filename='/home/studio/Dev/myrats/myrats/templates/component/login.mako'
_template_uri='/component/login.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n\n  \t<h1>Please log in:</h1>\n    <div class="loginform">\n    \t<form name="loginform" action="wheredoyougo" method="post">\n\t\t\t\t<table>\n\t\t\t\t\t<tr><td>Login:</td><td><input type="text" name="login" /></td></tr>\n\t\t\t\t\t<tr><td>Password:</td><td><input type="password" name="password" /></td></tr>\n\t\t\t\t</table>\n\t\t\t\t<input type="submit" value="Log in" />\n\t\t\t</form>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


