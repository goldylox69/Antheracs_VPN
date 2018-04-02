
import os
import subprocess
def clear():
	clear = os.system('./clear')
	print(clear)
def back():
	print("0) to go back")
	user = input(": ")
	if user in "0":
		print(part2())
def open():
	print(clear())
	os.system('./ram')
	print(part2())
def exit():
	print(quit())
def help():
	print(clear())
	print("Welcome to Help ")
	print(""" 

 ██░ ██ ▓█████  ██▓     ██▓███  
▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒
▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒
░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒
░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░
 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░     
 ░  ░░ ░   ░     ░ ░   ░░       
 ░  ░  ░   ░  ░    ░  ░         
                                

 """)
	print("""Antheracs is a VPN Free Service, 
VPN comes from VPNBOOK.com 

Username : vpnbook
Password : xf5s3d9

Antheracs may not work on all networks due to firewalls and network erros

created by Abraham Ramirez  """)
	print(back())	 
def standard():
	print(clear())
	print("Welcome to Standard VPN ")
	print(""" 

  ██████ ▄▄▄█████▓ ▄▄▄       ███▄    █ ▓█████▄ 
▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██ ▀█   █ ▒██▀ ██▌
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░░▒████▓ 
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ 
░  ░  ░    ░        ░   ▒      ░   ░ ░  ░ ░  ░ 
      ░                 ░  ░         ░    ░    
                                        ░      

 """)
	print(open())
def ghost():
	print(clear())
	print("Welcome to Ghost VPN ")
	print(""" 

  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓
 ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ 
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ 
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   
  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    
░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      
      ░  ░  ░  ░    ░ ░        ░           
                                           

 """)
	print("Warning: ready to run? Y/N ")
	user = input(":  ")
	if user in "y":
		print(" RUNNING NOW >>>>>")
		print(open())
def part2():
	print(clear())
	print(""" 

 ███▄ ▄███▓ ▄▄▄       ██▓ ███▄    █ 
▓██▒▀█▀ ██▒▒████▄    ▓██▒ ██ ▀█   █ 
▓██    ▓██░▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒
▒██    ▒██ ░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒
▒██▒   ░██▒ ▓█   ▓██▒░██░▒██░   ▓██░
░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒ 
░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░
░      ░     ░   ▒    ▒ ░   ░   ░ ░ 
       ░         ░  ░ ░           ░ 
                                    

""")
	print ("Welcome to Antheracs ")
	print("""Main Menu:

1) ghost mode
2) standard vpn
3) help

99) exit """)
	user = input(":  ")
	if user in "1":
		print (ghost())
	elif user in "2":
		print(standard())
	elif user in "3":
		print(help())
	elif user in "99":
		print(exit())
	else:
		print (main())
def main():
	print ("""

 ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ██░ ██  ▄▄▄     ▄▄▄█████▓
▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒
▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░
▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ 
░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░ 
░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░   
▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░   ░    
 ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░  ░  ░░ ░  ░   ▒    ░      
 ░          ░  ░     ░  ░░ ░      ░  ░    ░  ░  ░      ░  ░        
      ░                  ░                                         

 """)
	user = input("login: ")
	username = "goldylox"
	if user in username:
		print ("""Welcome to Antheracs VPN
			Created by Abraham Ramiez


The Following may be Ilegal on your network do you wish to continue?  """)
		answer = input("Do you wish to procced Y/N:  ")
		if answer in "y":
			print (part2())
		else: 
			print (main())

print(main())
