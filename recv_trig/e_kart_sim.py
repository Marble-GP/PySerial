import sys
import struct

RPM = 2500
CURR = 125.0
VOLT = 37.0
TRQ = 7.2

TEMP_INV = 50.0
TEMP_MOT = 65.5
VDC = 48.2

def func_stdout():
    senddata = []
    data:bytes = eval(sys.argv[1])
    check_sum = 0
    for i in range(len(data)-1):
        check_sum ^= data[i]
        check_sum &= 0xFF
    if data[-1] == check_sum:
        senddata = b""
        if int.from_bytes(data[0:2],"little") == 0x151:
            senddata += int(RPM).to_bytes(2, "little")
            senddata += int(CURR*10).to_bytes(2, "little")
            senddata += int(VOLT*10).to_bytes(2, "little")
            senddata += int(TRQ*100).to_bytes(2, "little")
    
        elif int.from_bytes(data[0:2],"little") == 0x161:
            senddata += int(TEMP_INV - 40).to_bytes(1, "little")
            senddata += int(TEMP_MOT - 40).to_bytes(1, "little")
            senddata += int(0).to_bytes(2, "little")
            senddata += int(VDC*10).to_bytes(2, "little")
            senddata += int(0).to_bytes(2, "little")
        
        elif int.from_bytes(data[0:2],"little") == 0x1A1:
            senddata += int(0).to_bytes(8, "little")

    print(senddata)#output to STDOUT
        


if len(sys.argv) == 2:
    func_stdout()