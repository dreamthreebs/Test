import urllib.request

# 打开网站
with urllib.request.urlopen('https://skyandtelescope.org/astronomy-resources/right-ascension-declination-celestial-coordinates/') as response:
   html = response.read()

# 将内容写入文件
with open('example.html', 'w') as f:
   f.write(html)
