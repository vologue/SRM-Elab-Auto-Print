import requests
import json
def login(sess):
    user=raw_input("Enter Reg No:")
    pas=raw_input("Enter Password:")
    creds='userid=%s&password=%s' %(user,pas)
    url="http://care.srmuniv.ac.in/ktrstudentskill/index.helper.php"
    header={
        'Host': 'care.srmuniv.ac.in',
        'Content-Length': '42',
        'Accept': '*/*',
        'Origin': 'http://care.srmuniv.ac.in',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://care.srmuniv.ac.in/ktrstudentskill/index.php',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cookie': '%s' %(sess[0]),
        'Connection': 'close',
    }
    response = requests.request("POST", url, data=creds, headers=header,allow_redirects=True)

url="http://care.srmuniv.ac.in/ktrstudentskill/index.php"
ind = requests.request("GET", url)
sess=ind.headers['Set-Cookie'].split(";")
login(sess)
for i in range (0,100):
    ref='http://care.srmuniv.ac.in/ktrstudentskill/login/studentnew/code/operating-systems/operating-systems.code.php?id=1&value=9'
    headers={
    'Host': 'care.srmuniv.ac.in',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': '%s' %ref,
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cookie': '%s' %sess[0],
    'Connection': 'close'
    }
    header2={
        'Host': 'care.srmuniv.ac.in',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cookie': '%s' %(sess[0]),
        'Connection': 'close'
    }
    url1='http://care.srmuniv.ac.in/ktrstudentskill/login/studentnew/code/operating-systems/operating-systems.code.php?id=1&value=%d' %i
    url='http://care.srmuniv.ac.in/ktrstudentskill/login/studentnew/code/getReport.php'
    print("Dowloading Report:%d" %i )
    r=requests.request("GET",url1,headers=header2)
    response = requests.request("POST", url, headers=headers)
    open('repo%d.png' %i, 'wb').write(response.content)
