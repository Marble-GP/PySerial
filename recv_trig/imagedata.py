#Auther: watanabe
#date: 2020/04/06
#brief: this is PyServer's receive-triger program sample-0

import sys
import cv2
import numpy as np

def func_stdout():
    buf = np.ones((900,600,3), np.uint8)*np.random.randint(255)
    print(buf.tobytes())

    #print(bytes(senddata))#output to STDOUT


if len(sys.argv) == 2:
    func_stdout()