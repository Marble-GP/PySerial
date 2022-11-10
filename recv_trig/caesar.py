#Auther: watanabe
#date: 2020/04/06
#brief: this is PyServer's receive-triger program sample-1

import sys

SHIFT = 10

def func_stdout():
    senddata = []
    data:bytes = eval(sys.argv[1])
    for uint8_ in data: #send-data processing
        senddata.append(0xFF&(uint8_ + SHIFT)) #convert to Caesar-cipher

    print(bytes(senddata)) #output to STDOUT
        


if len(sys.argv) == 2:
    func_stdout()