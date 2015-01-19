import urllib.request
import urllib.parse
import re
            
if __name__ == '__main__':
    stuno = input('please input id:')
    stupw = input('please input passwd:')
    webpage = urllib.request.urlopen('http://al.lib.xidian.edu.cn/F/?func=bor-info')

    body = webpage.read()
    body = body.decode('utf-8')
    pos = body.find('name="form1"')
    start = body.find('action="',pos)+len('action="')
    end = body.find('">',pos)
    url1 = body[start:end]
 #   print (url1)
    post = {}
    post['func']='login-session'
    post['login_source']='bor-info'
    post['bor_id']=stuno
    post['bor_verification']=stupw
    post['bor_library']='XDU50'
    post = urllib.parse.urlencode(post).encode('utf-8')

    response = urllib.request.urlopen(url1,post)

    body = response.read().decode('utf-8')

#    print (body)

    pos = body.find('width=35')
#    print pos
    start = body.find('replacePage(\'',pos)+len('replacePage(\'')
    end = body.find('\');">13',pos)
    url1 = body[start:end]

#    print(url1)

    body = urllib.request.urlopen(url1)

    html = body.read()
    html = html.decode('utf-8')
#    print(html)

    visit = []
    first = re.compile(r'<td class=td1 valign=top width="10%">(\d{8})')
    re_date = first.findall(html)
    for each in re_date:
            visit.append(each[0:4]+'年'+each[4:6]+'月'+each[6:8]+'日')


    name = []
    while 'width="27%"' in html:
        pos   = html.find('width="27%"')
        start = html.find('target=_blank>',pos)+len('target=_blank>')
        end   = html.find('</a></td>',pos)
        name.append(html[start:end])
        html  = html[end+len('width="27%"'):]

        
    print("题名            应还日期")
    for i in range(len(visit)):
        print("%s  %s" % (name[i],visit[i]))

    


   

    
