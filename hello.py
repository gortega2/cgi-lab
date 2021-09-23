#!/usr/bin/env python3

import os, json
import templates
print("Content-type:text/html\r\n\r\n")

print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")


print(os.environ)
json_object = json.dumps(dict(os.environ), indent=4)

for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        #print(f"<em>{param}</em> = {os.environ[param]}</li>")
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if (param=='HTTP_USER_AGENT'):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if(param=='HTTP_COOKIE'):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
        cookie_data = os.environ[param]
print(templates.login_page())
if 'Password=pong;' in cookie_data and 'Username=ping' in cookie_data:
    print(templates.secret_page('ping', 'pong'))


