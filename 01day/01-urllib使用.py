import urllib.request
url = "https://www.baidu.com"

response = urllib.request.urlopen(url)
print(response.status)