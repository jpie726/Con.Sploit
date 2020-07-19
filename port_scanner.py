from socket import *
from stringcolor import *
from time import *

def scan(ip):
	new = "yes"
def main():

	print(cs("   ___              __       _       _ _   \n  / __\___  _ __   / _\_ __ | | ___ (_) |_ \n / /  / _ \| '_ \  \ \| '_ \| |/ _ \| | __|\n/ /__| (_) | | | |__\ \ |_) | | (_) | | |_ \n\____/\___/|_| |_(_)__/ .__/|_|\___/|_|\__|\n                      |_|                  \n", "#FFFF33"))
	print(cs("1. I have the ip, stfu nurd\n2. I have the hostname, go away\n3. What in the god forsaken hell is ip or hostname?!?!?!\n\npress q or quit to exit", "#FF0000"))

	action = input(cs(">", "#169900"))
	ip = ""
	url = ""
	cont = "true"
	error = "Invalid operation, please try again" #169900

	if action == "1":
		print(cs("Input ip", "#7F1515"))
		ip = input(cs(">", "#169900"))
		scan(ip)
	elif action == "2":
		print(cs("Enter url", "#7F1515"))
		url = input(cs(">", "#169900"))
		ip = gethostbyname(url)
		if ip == "0.0.0.0":
			print("Error number 696969")
			sleep(10)
			quit()
		elif ip == "127.0.0.1":
			print("Error number 696969")
			sleep(10)
			quit()
		else:
			print("Ip address is " + ip + " from " + url)
	elif action == "3":
		print("Shut the hell up retard, stop faking stupidity. Oh wait, you're too much of a demented ass cockroach to even think of faking.")
		sleep(1)
		print("\nhttp://tiny.cc/IPvsHostname")
	elif action == "dbg":
		print("What error number did you get?")
		dumbass = input(cs(">", "#169900"))
		if dumbass == "696969":
			print("The website you entered did not translate to an ip address or pointed to yourself")
	elif action == "q" or "quit":
		quit()

	sleep(1)
	print("Scan again? y or yes/n or no")
	if again == "y" or "yes":
		main()
	elif again == "n" or "no":
		action = "no"

main()
