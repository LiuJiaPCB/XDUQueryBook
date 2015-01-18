# coding:utf-8
import requests
import re
from urllib import urlopen

        
    
    
if __name__ == '__main__':
    stuno = raw_input('please input id:')
    stupw = raw_input('please input passwd:')

    print "qerying,please wait..."
    s = requests.Session()

#    webpage = urlopen('http://al.lib.xidian.edu.cn/F/?func=bor-info')
    r = s.get('http://al.lib.xidian.edu.cn/F/?func=bor-info')
    body = r.text
#    body = webpage.read()
    
    pos = body.find('name="form1"')
    start = body.find('action="',pos)+len('action="')
    end = body.find('">',pos)
    url1 = body[start:end]
#    print url1
    post = {'func':'login-session','login_source':'bor-info','bor_id':stuno,'bor_verification':stupw,'bor_library':'XDU50'}

    r = s.post(url1,data = post)


    body = r.text

    pos = body.find('width=35')
#    print pos
    start = body.find('replacePage(\'',pos)+len('replacePage(\'')
    end = body.find('\');">8',pos)
    url1 = body[start:end]

 #   print url1

    body = s.get(url1)

    html = body.text

    visit = []

    first = re.compile(r'<td class=td1 valign=top width="10%">(\d{8})')
    visit.extend(first.findall(html))


    name = []
    while 'width="27%"' in html:
        pos   = html.find('width="27%"')
        start = html.find('target=_blank>',pos)+len('target=_blank>')
        end   = html.find('</a></td>',pos)
        name.append(html[start:end])
        html  = html[end+len('width="27%"'):]

    for i in range(len(visit)):
        print "%s        %s" % (name[i],visit[i])
    


   

    
