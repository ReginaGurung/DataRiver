import requests
import shutil
shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext')


r = requests.get('http://localhost:2113/web/index.html#/streams/dummy')

t = requests.get('http://www.hipstercode.com')

print(type(r))
print(r.text)
print(r.__getstate__)
#print(t.text)

outfile = open("test.txt","w")
outfile.write(r.text)



r = requests.post('http://localhost:2113/web/index.html#/streams/dummy', data=payload)