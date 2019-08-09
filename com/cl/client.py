# client2.py
#!/usr/bin/env python

import socket
import cv2

def send_img():
    filename='img.jpg'
    f = open(filename,'rb')
    while True:
        l = f.read(BUFFER_SIZE)
        while (l):
            s.send(l)
            #print('Sent ',repr(l))
            l = f.read(BUFFER_SIZE)
        if not l:
            f.close()
            # s.close()
            break
def get_img():
    with open('received_file.jpg', 'wb') as f:
        print ('file opened')
        while True:
            #print('receiving data...')
            data = s.recv(BUFFER_SIZE)
            # print('data=%s', (data))
            if not data:
                f.close()
                print ('file close()')
                break
            # write data to a file
            f.write(data)
    img = cv2.imread('received_file.jpg',1)
    cv2.imshow('a',img)
    cv2.waitKey(0)

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

check=''
while check != '4':
    flag = False
    msg = s.recv(BUFFER_SIZE)
    msg = msg.decode('utf-8')
    print(msg)
    response=input()
    if response == '3':
        flag = True
    check=response
    response=response.encode('utf-8')
    s.send(response)
    msg = s.recv(BUFFER_SIZE)
    msg = msg.decode('utf-8')
    print(msg)
    if flag:
        get_img()
        check='4'
    

print('Successfully get the file')
s.close()
print('connection closed')

