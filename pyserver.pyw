# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import os #get curdir
import subprocess #for receive-trigger
import json
import socket as sk
import threading as th

from time import sleep
from datetime import datetime




#settings-default
MAX_BUF_SIZE = 0xFFFF
TIMEOUT = 5.0
DELIMITER = " "
STR_ENCODE = "utf-8"


def hexstring_bytes(hexstr: str, delimiter=" "):
    cvtdata = hexstr.split(delimiter)
    return bytes(map(lambda s_:int(s_, base=16), cvtdata))

#communication init function
def sock_init(protocol :str, port :int) ->sk.socket:
    if protocol == "UDP":
        sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        sock.bind(("", port))
        return sock
    elif protocol == "TCP":
        sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        sock.bind(("", port))
        return sock


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyServer", pos = wx.DefaultPosition, size = wx.Size( 600,350 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL, name = u"PySerer" )
        self.data = b""
        self.CreateStatusBar()
        self.SetStatusText("")
        self.client = None

        self.udpsock = None
        self.tcpsock = None
        self.tcpsock_c = None

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DFACE ) )

        mainSizer = wx.GridSizer( 1, 2, 0, 0 )

        self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_READONLY )
        mainSizer.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )

        settingSizer = wx.BoxSizer( wx.VERTICAL )

        SendbackSizer = wx.BoxSizer( wx.VERTICAL )
        
        #self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Enable receive-triger program", wx.DefaultPosition, wx.DefaultSize, 0 )
        #SendbackSizer.Add( self.m_checkBox1, 0, wx.ALL, 5 )
        #SendbackSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"receive-trigger Program path", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        SendbackSizer.Add( self.m_staticText2, 0, wx.ALL, 5 )

        scriptSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,25 ), 0 )
        scriptSizer.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Refer", wx.DefaultPosition, wx.DefaultSize, 0 )
        scriptSizer.Add( self.m_button1, 0, wx.ALL, 5 )


        SendbackSizer.Add( scriptSizer, 1, wx.EXPAND, 5 )


        settingSizer.Add( SendbackSizer, 1, wx.EXPAND, 5 )

        self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"UDP", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        self.m_radioBtn6.SetValue(True)
        settingSizer.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

        self.m_radioBtn7 = wx.RadioButton( self, wx.ID_ANY, u"TCP", wx.DefaultPosition, wx.DefaultSize, 0 )
        settingSizer.Add( self.m_radioBtn7, 0, wx.ALL, 5 )

        portSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        portSizer.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 8080 )
        portSizer.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )


        #portSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        #self.m_button9 = wx.Button( self, wx.ID_ANY, u"reflesh", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        #portSizer.Add( self.m_button9, 0, wx.ALL, 5 )


        settingSizer.Add( portSizer, 1, wx.EXPAND, 5 )

        windowSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button4 = wx.Button( self, wx.ID_ANY, u"clear", wx.DefaultPosition, wx.Size( 50,25 ), 0 )
        windowSizer.Add( self.m_button4, 0, wx.ALL, 5 )

        self.m_radioBtn71 = wx.RadioButton( self, wx.ID_ANY, STR_ENCODE, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        self.m_radioBtn71.SetValue(True)
        windowSizer.Add( self.m_radioBtn71, 0, wx.ALL, 5 )

        self.m_radioBtn10 = wx.RadioButton( self, wx.ID_ANY, u"deci", wx.DefaultPosition, wx.DefaultSize, 0 )
        windowSizer.Add( self.m_radioBtn10, 0, wx.ALL, 5 )

        self.m_radioBtn8 = wx.RadioButton( self, wx.ID_ANY, u"hex", wx.DefaultPosition, wx.DefaultSize, 0 )
        windowSizer.Add( self.m_radioBtn8, 0, wx.ALL, 5 )


        settingSizer.Add( windowSizer, 1, wx.EXPAND, 5 )
        
        sendSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        sendSizer.Add( self.m_textCtrl6, 1, wx.ALL, 5 )
        
        sendcfgSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_radioBtn1x = wx.RadioButton( self, wx.ID_ANY, STR_ENCODE, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        sendcfgSizer.Add( self.m_radioBtn1x, 0, wx.ALL, 5 )

        self.m_radioBtn2x = wx.RadioButton( self, wx.ID_ANY, u"hex", wx.DefaultPosition, wx.DefaultSize, 0 )
        sendcfgSizer.Add( self.m_radioBtn2x, 0, wx.ALL, 5 )

        sendSizer.Add(sendcfgSizer, 1, wx.EXPAND, 5)
        
        self.m_button91 = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button91.Enable(False)
        sendSizer.Add( self.m_button91, 0, wx.ALL, 5 )



        settingSizer.Add( sendSizer, 1, wx.EXPAND, 5 )


        ControlSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.actionflg = False
        ControlSizer.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        ControlSizer.Add( self.m_button3, 0, wx.ALL, 5 )


        settingSizer.Add( ControlSizer, 1, wx.EXPAND, 5 )


        mainSizer.Add( settingSizer, 1, wx.EXPAND, 5 )


        self.SetSizer( mainSizer )
        self.Layout()

        self.Centre( wx.BOTH )


        self.refleshflg = False
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.fileWindow )
        #self.m_button9.Bind( wx.EVT_BUTTON, self.reflesh )
        self.m_button4.Bind( wx.EVT_BUTTON, self.clear )
        self.m_button2.Bind( wx.EVT_BUTTON, self.action )
        self.m_button3.Bind( wx.EVT_BUTTON, self.showsave )
        self.m_button91.Bind( wx.EVT_BUTTON, self.send_btn)


        #my code

        self.looptask_udp = th.Thread(target=self.UDP_server)
        self.looptask_tcp = th.Thread(target=self.TCP_server)
        self.looptask_tcp.setDaemon(True)
        self.looptask_udp.setDaemon(True)
        self.looptask_udp.start()
        self.looptask_tcp.start()
        


        self.Bind(wx.EVT_CLOSE, self.ExitHandler)



    def __del__( self ):
        pass
    

    def ExitHandler(self, event):
        event.Skip()
        self.Destroy()
        exit(0)

    # Virtual event handlers, overide them in your derived class
    def fileWindow( self, event ):
        event.Skip()
        pathwdw = wx.FileDialog(None,wildcard="python Files(*.py)|*.py", defaultDir=os.curdir)
        if pathwdw.ShowModal() == wx.ID_OK:
            self.m_textCtrl3.Value = pathwdw.GetPath()
            pathwdw.Close()
        else:
            pass


    def reflesh( self, event ):
        event.Skip()


    def clear( self, event ):
        event.Skip()
        self.m_textCtrl9.SetValue("")
        self.m_textCtrl6.SetValue("")

    def action( self, event ):
        if self.actionflg:
            self.m_radioBtn6.Enable(True)
            self.m_radioBtn7.Enable(True)
            self.m_spinCtrl1.Enable(True)
            self.m_button91.Enable(False)
            self.actionflg = False
            try:
                if self.m_radioBtn6.Value:#UDP
                    self.udpsock.close()
                    self.SetStatusText("UDP socket is closed.")
                elif self.m_radioBtn7.Value:#TCP
                    self.tcpsock.close()
                    self.SetStatusText("TCP socket is closed.")
            except OSError:
                pass

            self.m_button2.SetLabelText("Start")
        else:
            self.m_radioBtn6.Enable(False)
            self.m_radioBtn7.Enable(False)
            self.m_spinCtrl1.Enable(False)
            self.m_button91.Enable(True)
            self.actionflg = True
            self.m_button2.SetLabelText("Stop")
        event.Skip()

    def showsave( self, event ):
        #dialog = MyDialog1(self, self.m_textCtrl9.Value)
        #dialog.Show()
        event.Skip()
        now_ts = datetime.now()
        timestr = str(now_ts.year)+"_"+str(now_ts.day)+"_"+str(now_ts.hour)+str(now_ts.minute)+str(now_ts.second)
        dialog = wx.FileDialog(self, defaultDir=os.curdir, defaultFile="pyserverlog"+timestr+".txt")
        if dialog.ShowModal() == wx.ID_OK:
            with open(dialog.GetPath(), "w") as f:
                f.write(self.m_textCtrl9.Value)
            wx.MessageBox("Save successfull.")
    
    def send_btn(self, event):
        if self.actionflg:
            try:
                if self.m_radioBtn6.GetValue():#UDP
                    if self.m_radioBtn1x.GetValue():#UTF-8
                        senddata = bytes(self.m_textCtrl6.GetValue(), STR_ENCODE)
                        sendlen = self.udpsock.sendto(senddata, self.client)

                    elif self.m_radioBtn2x.GetValue():#hex mode
                        sendtxtdata:str = self.m_textCtrl6.GetValue()
                        senddata = hexstring_bytes(sendtxtdata, DELIMITER)
                        sendlen = self.udpsock.sendto(senddata, self.client)                        

                
                elif self.m_radioBtn7.GetValue():#TCP
                    if self.m_radioBtn1x.GetValue():#UTF-8
                        senddata = bytes(self.m_textCtrl6.GetValue(), STR_ENCODE)
                        sendlen = self.udpsock.sendto(senddata, self.client)

                    elif self.m_radioBtn2x.GetValue():#hex mode
                        sendtxtdata:str = self.m_textCtrl6.GetValue()
                        senddata = hexstring_bytes(sendtxtdata, DELIMITER)
                        sendlen = self.udpsock.sendto(senddata, self.client)
            except TypeError or AttributeError:
                wx.MessageBox("Sending failed. (No client)")
                return
            except ValueError:
                wx.MessageBox("Text convert failed. (delimiter=\"{}\")".format(DELIMITER))
                return

            #wx.MessageBox("{} bytes have been sent.".format(sendlen))
            self.SetStatusText("send: {}".format(senddata))

        else:
            wx.MessageBox("First of all, click \"Start\".")



    def UDP_server(self):
        while True:
            if self.m_radioBtn6.GetValue() and self.actionflg:#is UDP mode

                try:
                    self.tcpsock_c.close()
                    self.tcpsock.close()
                except AttributeError:
                    pass
                
                print(self.m_spinCtrl1.GetValue())
                self.udpsock = sock_init("UDP", self.m_spinCtrl1.GetValue())
                self.SetStatusText("Inirialize UDP socket.")


                while self.m_radioBtn6.GetValue() and self.actionflg:#while UDP-mode&Act-mode
                    try:
                        recvinfo = self.udpsock.recvfrom(MAX_BUF_SIZE)
                    except OSError:
                        break

                    self.data = recvinfo[0]
                    self.client = recvinfo[1]

                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = subprocess.SW_HIDE
                    with subprocess.Popen(["python", self.m_textCtrl3.GetValue(), str(self.data)],startupinfo=startupinfo , stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as sp:
                        sp.wait()
                        try:
                            ifget = eval(sp.communicate()[0])
                        except SyntaxError:
                            ifget = None

                        #$python Arbitrary_code. bytes(data) -> response-read from stdout
                        if not(ifget == b"" or ifget == None):
                            self.udpsock.sendto(ifget, self.client)
                            self.SetStatusText("Send back: {}".format(ifget))
                        else:
                            self.SetStatusText("No send back data.")

                    #Put data
                    if self.m_radioBtn71.GetValue():#string-mode
                        self.m_textCtrl9.Value += self.data.decode(STR_ENCODE, "replace")
                    elif self.m_radioBtn10.GetValue():#decimal-mode
                        for _char in self.data:
                            self.m_textCtrl9.Value += str(_char)+DELIMITER
                    elif self.m_radioBtn8.GetValue():#hex-mode
                        for _char in self.data:
                            self.m_textCtrl9.Value += hex(_char)+DELIMITER
                        

                        sleep(0.001)#1ms
                self.udpsock.close()
                self.udpsock = None
                self.client = None
            else: 
                sleep(0.01)#10ms


    def TCP_server(self):
        while True:
            if self.actionflg and self.m_radioBtn7.GetValue():

                try:
                    self.udpsock.close()
                except AttributeError:
                    pass
                

                self.tcpsock = sock_init("TCP", self.m_spinCtrl1.GetValue())
                self.SetStatusText("Inirialize TCP socket.")
                try:
                    self.tcpsock.listen(5)
                    accinfo = self.tcpsock.accept()
                    self.tcpsock_c = accinfo[0]
                    self.client = accinfo[1]
                    self.tcpsock_c.settimeout(TIMEOUT)
                except OSError:
                    break

                
                while self.actionflg and self.m_radioBtn7.GetValue():
                    try:
                        recvinfo = self.udpsock.recvfrom(MAX_BUF_SIZE)
                    except OSError:
                        break

                    self.data = recvinfo[0]
                    self.client = recvinfo[1]

                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = subprocess.SW_HIDE
                    with subprocess.Popen(["python", self.m_textCtrl3.GetValue(), str(self.data)],startupinfo=startupinfo , stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as sp:
                        sp.wait()
                        try:
                            ifget = eval(sp.communicate()[0])
                        except SyntaxError:
                            ifget = None

                        #$python Arbitrary_code. bytes(data) -> response-read from stdout
                        if not(ifget == b"" or ifget == None):
                            self.udpsock.sendto(ifget, self.client)
                            self.SetStatusText("Send back: {}".format(ifget))
                        else:
                            self.SetStatusText("No send back data.")

                    #Put data
                    if self.m_radioBtn71.GetValue():#string-mode
                        self.m_textCtrl9.Value += self.data.decode(STR_ENCODE, "replace")
                    elif self.m_radioBtn10.GetValue():#decimal-mode
                        for _char in self.data:
                            self.m_textCtrl9.Value += str(_char)+DELIMITER
                    elif self.m_radioBtn8.GetValue():#hex-mode
                        for _char in self.data:
                            self.m_textCtrl9.Value += hex(_char)+DELIMITER
                    
                    sleep(0.001)
                
                self.tcpsock_c.close()
                self.client = None
                self.tcpsock.close()
                self.tcpsock = None
            sleep(0.01)

                

    def frameLoop(self):
        while True:
            self.udpsock = sock_init("UDP", self.m_spinCtrl1.GetValue())
            while self.actionflg:
                if self.m_radioBtn6.GetValue():#UDP
                    recvinfo = self.udpsock.recvfrom(MAX_BUF_SIZE)
                    self.data = recvinfo[0]
                    self.client = recvinfo[1]

                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = subprocess.SW_HIDE
                    with subprocess.Popen(["python", self.m_textCtrl3.GetValue(), str(self.data)],startupinfo=startupinfo , stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as sp:
                        sp.wait()
                        try:
                            ifget = eval(sp.communicate()[0])
                        except SyntaxError:
                            ifget = None
                    #$python Arbitrary_code. bytes(data) -> response-read from stdout
                    if not(ifget == b"" or ifget == None):
                        self.udpsock.sendto(ifget, self.client)
                        self.SetStatusText("Send back: {}".format(ifget))
                    else:
                        self.SetStatusText("No send back data.")
                        

                    if self.m_radioBtn71.GetValue():#string
                        self.m_textCtrl9.Value += self.data.decode(STR_ENCODE, "replace")
                    elif self.m_radioBtn10.GetValue():#decimal
                        for _char in self.data:
                            self.m_textCtrl9.Value += str(_char)+DELIMITER
                    elif self.m_radioBtn8.GetValue():#hex
                        for _char in self.data:
                            self.m_textCtrl9.Value += hex(_char)+DELIMITER

                elif self.m_radioBtn7.GetValue(): #TCP*********************************************************
                    self.tcpsock = sock_init("TCP", self.m_spinCtrl1.GetValue())
                    self.tcpsock.listen(1)
                    accinfo = self.tcpsock.accept()
                    self.tcpsock_c = accinfo[0]
                    self.client = accinfo[1]

                    self.tcpsock_c.settimeout(TIMEOUT)
                    while True:
                        try:
                            self.data = self.tcpsock_c.recv(MAX_BUF_SIZE)
                            startupinfo = subprocess.STARTUPINFO()
                            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                            startupinfo.wShowWindow = subprocess.SW_HIDE
                            with subprocess.Popen(["python", self.m_textCtrl3.GetValue(), str(self.data)],startupinfo=startupinfo , stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as sp:
                                sp.wait()
                                try:
                                    ifget = eval(sp.communicate()[0])
                                except SyntaxError:
                                    ifget = None
                            #$python Arbitrary_code. bytes(data) -> response-read from stdout

                            if not(ifget == b"" or ifget == None):
                                self.udpsock.sendto(ifget, self.client)
                                self.SetStatusText("Send back: {}".format(ifget))
                            else:
                                self.SetStatusText("No send back data.")
                        except sk.timeout or sk.error or self.refleshflg:
                            print("TCP connection end")
                            break

                        if self.m_radioBtn71.GetValue():#string
                            self.m_textCtrl9.Value += self.data.decode(STR_ENCODE, "replace")
                        elif self.m_radioBtn10.GetValue():#decimal
                            for _char in self.data:
                                self.m_textCtrl9.Value += str(_char)+DELIMITER
                        elif self.m_radioBtn8.GetValue():#hex
                            for _char in self.data:
                                self.m_textCtrl9.Value += hex(_char)+DELIMITER
                        
                        sleep(0.001)

                    self.tcpsock_c.close()
                    self.tcpsock.close()
                    self.client = None
                sleep(0.001)
                
            sleep(0.001)
            self.udpsock.close()
            self.client = None

            


###########################################################################
## Class MyDialog1
###########################################################################
class MyDialog1(wx.Dialog):
    def __init__( self, parent, txtdata ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Save", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.data = txtdata

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"text", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

        self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"CSV", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_radioBtn6, 0, wx.ALL, 5 )
        self.m_radioBtn6.Enable(enable=False)

        self.m_radioBtn11 = wx.RadioButton( self, wx.ID_ANY, u"TSV", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_radioBtn11, 0, wx.ALL, 5 )
        self.m_radioBtn11.Enable(enable=False)


        bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"File path", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), 0 )
        bSizer9.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, u"Refer", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
        bSizer9.Add( self.m_button7, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button5 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button5, 0, wx.ALL, 5 )

        self.m_button6 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button6, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )

        self.m_button5.Bind(wx.EVT_BUTTON, self.bt_OK)
        self.m_button6.Bind(wx.EVT_BUTTON, self.bt_Cancel)
        self.m_button7.Bind(wx.EVT_BUTTON, self.refer)


        self.SetSizer( bSizer6 )
        self.Layout()
        bSizer6.Fit( self )

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    def refer(self, event):
        event.Skip()
        pathwdw = wx.FileDialog(None,defaultDir=os.curdir)
        if pathwdw.ShowModal() == wx.ID_OK:
            self.m_textCtrl3.SetValue(pathwdw.GetPath())
            pathwdw.Close()
        else:
            pass

    def bt_OK(self, event):
        with open(self.m_textCtrl3.Value, "w") as sf:
            sf.write(self.data)
        event.Skip()
        self.Close()

    def bt_Cancel(self, event):
        self.Close()
        event.Skip()



if __name__ == "__main__":
    with open("config.json", "r") as conf:
        cfgdata :dict = json.load(conf)
        MAX_BUF_SIZE = cfgdata["MAX_BUF_SIZE"]
        TIMEOUT = cfgdata["TCP_TIMEOUT"]
        DELIMITER = cfgdata["DELIMITER"]
        STR_ENCODE = cfgdata["STR_ENCODE"]

    app = wx.App(0, useBestVisual=True)
    try:
        frame = MyFrame1(None)
        app.SetTopWindow(frame)
        frame.Show()
    except:
        frame.Destroy()
        app.Destroy()
        exit(0)
    app.MainLoop()



