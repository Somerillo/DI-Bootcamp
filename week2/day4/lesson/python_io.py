#old school: not so good: we needed to "manually" close the file

# f = open('sample.txt', 'r+') #open('complete file name - with extension', 'mode)
# content = f.read()
# print(content)
# f.close()

# try:
#     f = open('sample.txt', 'r+') #open('complete file name - with extension', 'mode)
#     content = f.read()
#     print(content)
# finally:
#     f.close()

#After python 2.5 version we have a magic keyword to close automatically the file: 'with"

with open(r"C:\Users\julia\OneDrive\Documents\DI-Bootcamp-web148-149\sample.txt", 'a+', encoding= 'utf-8') as f:
    for i in range(10):
        f.write(f'this is line {i}\n')
    f.seek(0)
    content = f.read()
    print(content)

