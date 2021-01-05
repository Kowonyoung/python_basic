#위치파라미터
def connect(server, port):
    url = f'http://{server}:{port}'
    return url

print(connect('localhost','8080'))
print(connect(port = '80', server = 'aa.com'))
print(connect('naver.com', port = '8090'))

#Argument Default value
