#!/usr/bin/env python3 
import cgi, cgitb
import secret
import templates
import time
import os

form = cgi.FieldStorage()

usrnm = form.getvalue('username')
passwd = form.getvalue('password')
#'''
if (form.getvalue('username')=='ping') and (form.getvalue('password') == 'pong'):
    print("Set-Cookie:lastvisit=" + str(time.time()) +';')
    print("Set-Cookie:Password=%s" %('pong') +';')
    print("Set-Cookie:Username=%s" %('ping') +';')
    #print("<html><p>idk what im doing</p></html>")
else:
    templates.after_login_incorrect()
#'''
print("Content-type:text/html\r\n\r\n")

print(templates.secret_page(username=usrnm, password=passwd))
print("<html>")
print("<p><b>Username:</b> %s <b>Password:</b> %s</p>" % (usrnm, passwd))

print("</html>")