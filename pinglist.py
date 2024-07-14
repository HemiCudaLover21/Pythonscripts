import os
import platform
print("ping a list of websites from text file in your directory. Windows or Linux OSes only.")
print("welcome to pinglist. To ping a list of domains or ip addresses supply a list with each website on a newline.\n")
file = input("put the name of the file (in the same directory) to open:")
fileopen = open(str(file))
websitelist = []
windowstrue = 0
linuxtrue = 0
othertrue = 0

def check_ping_windows(hostname):
	response = os.system("ping -n 1 " + hostname)
	if response == 0:
		pingstatus = True
	else:

		pingstatus = False
	return pingstatus

def check_ping_linux(hostname):
	response = os.system("ping -c 1 " + hostname)
	if response == 0:
		pingstatus = True
	else:

		pingstatus = False
	return pingstatus

osver = platform.system()

if osver == 'Windows':
	with fileopen as text:
		text_contents = text.readlines()
		print(text_contents)
		for i in text_contents:
			websitelist.append(i[:-1])
		for j in websitelist:
			check_ping_windows(j)

if osver == 'Linux':
		with fileopen as text:
			text_contents = text.readlines()
			print(text_contents)
			for i in text_contents:
				websitelist.append(i[:-1])
			for j in websitelist:
				check_ping_linux(j)

if osver not in ('Linux', 'Windows'):
    print("Your OS isn't supported.")
