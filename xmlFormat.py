import glob

xmlFilePath = glob.glob(r'xml/*')

print(xmlFilePath)

for _ in xmlFilePath:
    with open(_, 'r') as r:
        lines = r.readlines()
    with open(_, 'w') as w:
        w.write('<all>')
        for l in lines:
           if '<?xml version="1.0" encoding="utf-8"?>' not in l:
              w.write(l)
        w.write('</all>')