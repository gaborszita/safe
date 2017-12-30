#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'

def mainprogram():
    # Enter password here
    Password = 'mypassword'
    formData = cgi.FieldStorage()
    action = formData.getvalue('action')
    passwd = formData.getvalue('passwd')
    if action == 'login' and passwd == Password:
        f = open('/home/pi/safe/code.txt')
        code = f.read()
        f.close()
        print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type" />
  <meta name="viewport"
 content="width=device-width, initial-scale=1" />
  <title>Raspberry pi safe</title>
</head>
<body>
<h1 style="text-align: center;">Raspberry pi safe</h1>
code: """ + code + """<br />
<br />
<br />
<form method="post" action="./safeweb.py">
  <table style="text-align: left;">
    <tbody>
      <tr>
        <td>New code: </td>
        <td><input name="newcode" type="number" required /><br />
        </td>
      </tr>
    </tbody>
  </table>
  <input value="Change code" type="submit" /><input
 name="action" value="changecode" type="hidden" /><input
 name="securety" value="TghXCDre54ncDDAG7cxrDsRdCsfdGg"
 type="hidden" /></form>
</body>
</html>"""
    elif action == 'login' and passwd != Password:
        print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" /><title>Raspberry pi safe</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
<h1 style="text-align: center;">Raspberry pi safe</h1>
<form method="post" action="/cgi-bin/safeweb.py">
<table style="text-align: left;">
<tbody>
<tr>
<td>Password:</td>
<td></td>
<td><input name="passwd" type="password" /></td>
</tr>
</tbody>
</table>
<input value="Login" type="submit" /><p>Password incorrect</p><input name="action" value="login" type="hidden" /><br />
</form>
</body>
</html>"""
    elif action == 'changecode':
        securety = formData.getvalue('securety')
        if securety == 'TghXCDre54ncDDAG7cxrDsRdCsfdGg':
            newcode = formData.getvalue('newcode')
            if len(newcode) == 6:
                f = open('/home/pi/safe/code.txt', 'w')
                f.write(newcode)
                f.close()
                code = newcode
                print"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta content="text/html; charset=ISO-8859-1"http-equiv="content-type" />
    <meta name="viewport"content="width=device-width, initial-scale=1" />
    <title>Raspberry pi safe</title>
    </head>
    <body onload="alert('Code changed successfully!')">
    <h1 style="text-align: center;">Raspberry pi safe</h1>
    code: """ + code + """<br />
    <br />
    <br />
    <form method="post" action="./safeweb.py">
    <table style="text-align: left;">
    <tbody>
    <tr>
    <td>New code: </td>
    <td><input name="newcode" type="number" required /><br />
    </td>
    </tr>
    </tbody>
    </table>
    <input value="Change code" type="submit" /><input
    name="action" value="changecode" type="hidden" /><input
    name="securety" value="TghXCDre54ncDDAG7cxrDsRdCsfdGg"
    type="hidden" /></form>
    </body>
    </html>"""
            else:
                f = open('/home/pi/safe/code.txt')
                code = f.read()
                f.close()
                print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta content="text/html; charset=ISO-8859-1"
    http-equiv="content-type" />
    <meta name="viewport"
    content="width=device-width, initial-scale=1" />
    <title>Raspberry pi safe</title>
    </head>
    <body onload="alert('Code invalid!')">
    <h1 style="text-align: center;">Raspberry pi safe</h1>
    code: """ + code + """<br />
    <br />
    <br />
    <form method="post" action="./safeweb.py">
    <table style="text-align: left;">
    <tbody>
    <tr>
    <td>New code: </td>
    <td><input name="newcode" type="number" required /><br />
    </td>
    </tr>
    </tbody>
    </table>
    <input value="Change code" type="submit" /><input
    name="action" value="changecode" type="hidden" /><input
    name="securety" value="TghXCDre54ncDDAG7cxrDsRdCsfdGg"
    type="hidden" /></form>
    </body>
    </html>"""

mainprogram()
