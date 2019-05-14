import base64

fr = open('./maria_ozawa.jpg', mode='rb')
fw = open('./maria_ozawa.b64_5.jpg', mode ='wb')
fw.write(base64.b64decode(fr.read()))
print(fr,fw)