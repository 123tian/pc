import urllib.parse
import urllib.request
import re
import os
class TieBasipder():
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?'
        self.turl = 'https://tieba.baidu.com/'
        self.headers = {
            'User - Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400'

        }

    def send_request(self,url):
        request = urllib.request.Request(url=url,headers=self.headers)
        response = urllib.request.urlopen(request )
        if response.status  ==200:
            content = response.read()
            return content

        else:
            print('出错了',response.status)


    def parse_detail(self,content):
        pattern =re.compile(r'<img.*?class="BDE_Image".*?scr"(.*?)".*?>',re.S)
        pic_list = re.findall(pattern,content)
        for pic in pic_list:
            content = self.send_pic_request(pic)
            name = pic[-2]
            self.write_content(content,name)

    def parse(self,content):
        pattern = re.compile(r'<a\srel="noreferrer"\shref="(/p/.*?)"',re.S)
        link_list = re.findall(pattern,content)
        for link in link_list:
            detail_url = self.turl+link
            print(detail_url)
            content = self.send_detail_request(detail_url).decode('utf8')

    def write_content(self,content,name):
        print('正在存在%s'%name)
        path ='tieba'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path +''+name,'wb')as f:
            f.write(content)

    def write_html(self,content):
        with open('tieba.html','wb')as f:
            f.write(content)

    def start(self):
        kw = input('请输入你要爬取的名字')
        page = int(input('请输入你要爬取多少页'))
        for i in range(1,page+1):
            pn = (i-1)*50
            keyword = {'kw':kw,'pn': pn}
            result= urllib.parse.urlencode(keyword)
            full_url = self.url+result
            content = self.send_request(full_url).decode('utf8')
            self.parse(content)

    '''
    https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=50
    '''

if __name__ == '__main__':
    tbs = TieBasipder()
    tbs.start()

    '''
    r'<a.*?rel="noreferrer".*?href="(.*?)"'>
    '''