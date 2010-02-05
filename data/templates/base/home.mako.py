from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1265338172.799705
_template_filename='/home/studio/Dev/myrats/myrats/templates/base/home.mako'
_template_uri='/base/home.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n  \n<html>\n    <head>\n        <title>myRaTS</title>\n        Welcome on myRaTS - Process Manager for Repair and Technical Services\n<!--        ')
        # SOURCE LINE 8
        runtime._include_file(context, '/component/login.mako', _template_uri)
        __M_writer(u' -->\n    </head>\n  \n    <body>\n    <h1>')
        # SOURCE LINE 12
        __M_writer(escape(self.title()))
        __M_writer(u'</h1>\n    ')
        # SOURCE LINE 13
        __M_writer(escape(next.body()))
        __M_writer(u'\n    </body>\n</html>\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(escape(c.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


