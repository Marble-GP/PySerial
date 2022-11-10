#Auther: watanabe
#date: 2020/04/06
#brief: this is PyServer's receive-triger program sample-0

import sys

def func_stdout():
    senddata = []
    data:bytes = eval(sys.argv[1])
    for uint8_ in data: #send-data processing
        senddata.append(uint8_)

    print(bytes(senddata))#output to STDOUT
        


if len(sys.argv) == 2:
    func_stdout()