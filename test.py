
file = open('test.html', 'r')
filewrite = open ('winnie2.html', 'wb')
lines = file.readlines()
linestemp = []
for i in xrange(len(lines)):
    line = lines[i]
    if line.startswith('http'):
        linestemp.append('<a href="' + line + '" style="text-decoration:none" target="_blank">' + line + '</a><br>\n')
    elif line.startswith('\n'):
        linestemp.append('<br><br>\n\n')
    elif line.startswith('follow'):
        linestemp.append('<span style="font-size: small; color: rgb(91,155,213); ">' + line + '</span><br>\n')
    elif line.startswith('like'):
        linestemp.append('<span style="font-size: small; color: rgb(91,155,213); ">' + line + '</span><br>\n')
    elif line.startswith('favorite'):
        linestemp.append('<span style="font-size: small; color: rgb(91,155,213); ">' + line + '</span><br>\n')
    else:
        linestemp.append('<b>' + line + '</b><br>\n')

for line in linestemp:
    filewrite.write(line)

file.close()
filewrite.close()





class item:
    def __init__(self, title, url, enter):
        self.title = title + '<br>'
        self.url = url + '<br>'
        self.enter = enter + '<br><br>'

    