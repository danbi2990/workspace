import textract

file = '/Users/jake/OneDrive - leverage innovative users/Documents/비리유치원/Busan-report.pdf'

text = textract.process(file, layout=True)

with open('/Users/jake/OneDrive - leverage innovative users/Documents/비리유치원/busan.txt', 'wb') as f:
    f.write(text)

# print(text[:100].decode('utf-8'))
