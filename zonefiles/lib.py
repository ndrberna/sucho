import time
import queue
import sys
from bs4 import BeautifulSoup
sys.setrecursionlimit(10000) 
from os import getpid
import random
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.parse import urlparse
from googletrans import Translator


translator = Translator()
def getTranslateGoogle(text):
    translation =""
    try:
        translation=translator.translate(text, dest="en")
        #print(translation)
        return (translation.text)
    except:
        return ("")

def is_http_or_https(url):
    return urlparse(url).scheme in {'http', 'https'}

headers_list=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]


def connectUrl(url):
    headers = {'user-agent': random.choice(headers_list)}
    session = requests.Session()
    retry = Retry(connect=1, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    try:
        r  = requests.get(url, allow_redirects = True, headers=headers, timeout=10)
        if r.status_code==200:
            print(url)
            return r
        else:
            
            return r
    except:
        
        return ("")
    
def parseUrl(baseurl):
    if is_http_or_https(baseurl):
        url = baseurl
        r=connectUrl(url)
        return (r)
    else:
        if baseurl.startswith("www"):
            prefix=["https://","http://"]
            for i in prefix:
                url = i+baseurl
                r=connectUrl(url)
                if r:
                    return (r)
                    break
        else:
            prefix=["https://","http://","https://www.","http://www."]

            for i in prefix:
                url = i+baseurl
                r=connectUrl(url)
                if r:
                    return (r)
                    break
                    
def analyzeUrl(url): 
    print(url)
    r=parseUrl(url)
    size=""
    lang=""
    title=""
    soup=""
    try:
        if r:
            if r.status_code==200:
                data = r.text
                soup = BeautifulSoup(data, 'lxml')
                lang=""
                try:
                    size=int(r.headers['content-length'])
                    lang=soup.html["lang"]
                except:
                    pass
                for soup_title in soup.find_all('title'):
                        title=soup_title.text
            #print(url,r.status_code,title,lang,size)
            return url,r.status_code,title,lang,size
        #print (url,"","","","")
    except:
        pass
    return url,"","","",""    
