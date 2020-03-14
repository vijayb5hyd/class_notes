
# import tkinter module 
from tkinter import *
  
# import other necessery modules 
import random 
import time 
import datetime 
  
# creating app_window object 
app_window = Tk() 
  
# defining size of window 
app_window.geometry("1200x6000") 
  
# setting up the title of window 
app_window.title("App to Encrypt/Decrypt a message.") 
  
TopFrame = Frame(app_window, width = 1600, relief = GROOVE) 
TopFrame.pack(side = TOP) 
  
LeftFrame = Frame(app_window, width = 800, height = 700, relief = GROOVE) 
LeftFrame.pack(side = LEFT) 

localtime = time.asctime(time.localtime(time.time())) 
  
lblInfo = Label(TopFrame, font = ('arial', 40, 'bold'), text = "TKinter GUI App \n Encrypt/Decrypt My Password", fg = "blue", bd = 10, anchor='w')                        
lblInfo.grid(row = 0, column = 0) 
  
lblInfo = Label(TopFrame, font=('arial', 16, 'bold'), text = localtime, fg = "green", bd = 10, anchor = 'w')                         
lblInfo.grid(row = 1, column = 0) 
  
name = StringVar() 
msg = StringVar() 
key = StringVar() 
mode = StringVar() 
result = StringVar() 
  
# exit function 
def qExit(): 
    app_window.destroy() 
  
# Function to reset the window 
def Reset(): 
    name.set("") 
    msg.set("") 
    key.set("") 
    mode.set("") 
    result.set("") 
  
  
# reference 
lblReference = Label(LeftFrame, font = ('arial', 16, 'bold'), text = "Name/User:", bd = 16, anchor = "w")                  
lblReference.grid(row = 0, column = 0) 
  
txtReference = Entry(LeftFrame, font = ('arial', 16, 'bold'), textvariable = name, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')                         
txtReference.grid(row = 0, column = 1) 
  
# labels 
lblmsg = Label(LeftFrame, font = ('arial', 16, 'bold'), text = "Message/Password:", bd = 16, anchor = "w")       
lblmsg.grid(row = 1, column = 0) 
  
txtmsg = Entry(LeftFrame, font = ('arial', 16, 'bold'), textvariable = msg, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')                
txtmsg.grid(row = 1, column = 1) 
  
lblkey = Label(LeftFrame, font = ('arial', 16, 'bold'), text = "Key:", bd = 16, anchor = "w")         
lblkey.grid(row = 2, column = 0) 
  
txtkey = Entry(LeftFrame, font = ('arial', 16, 'bold'), textvariable = key, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')                 
txtkey.grid(row = 2, column = 1) 
  
lblmode = Label(LeftFrame, font = ('arial', 16, 'bold'), text = "Mode(e for encrypt, d for decrypt):", bd = 16, anchor = "w")                                
lblmode.grid(row = 3, column = 0) 
  
txtmode = Entry(LeftFrame, font = ('arial', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')                    
txtmode.grid(row = 3, column = 1) 
  
lblService = Label(LeftFrame, font = ('arial', 16, 'bold'), text = "The result:", bd = 16, anchor = "w")            
lblService.grid(row = 2, column = 2) 
  
txtService = Entry(LeftFrame, font = ('arial', 16, 'bold'),  textvariable = result, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')                          
txtService.grid(row = 2, column = 3) 
  
# Vigenère cipher 
import base64 
  
# Function to encode 
def encode(key, clear): 
    enc = [] 
      
    for i in range(len(clear)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256) 
                       
        enc.append(enc_c) 
          
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
  
# Function to decode 
def decode(key, enc): 
    dec = [] 
      
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 
  
  
def Ref(): 
    print("Message= ", (msg.get())) 
  
    clear = msg.get() 
    k = key.get() 
    m = mode.get() 
  
    if (m == 'e'): 
        result.set(encode(k, clear)) 
    else: 
        result.set(decode(k, clear)) 
  
# Show message button 
btnTotal = Button(LeftFrame, padx = 16, pady = 8, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Show Message", bg = "powder blue", command = Ref).grid(row = 7, column = 1) 
  
# Reset button 
btnReset = Button(LeftFrame, padx = 16, pady = 8, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Reset", bg = "green", command = Reset).grid(row = 7, column = 2) 
  
# Exit button 
btnExit = Button(LeftFrame, padx = 16, pady = 8, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Exit", bg = "red", command = qExit).grid(row = 7, column = 3) 
  
# keeps window alive 
app_window.mainloop() 
