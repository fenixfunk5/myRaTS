<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
  
<html>
    <head>
        <title>myRaTS</title>
        Welcome on myRaTS - Process Manager for Repair and Technical Services
<!--        <%include file="/component/login.mako" /> -->
    </head>
  
    <body>
    <h1>${self.title()}</h1>
    ${next.body()}
    </body>
</html>
  
<%def name="title()">${c.title}</%def>