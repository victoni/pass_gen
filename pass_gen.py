#!/usr/bin/env python3
import sys, pyperclip, argparse
from getpass import getpass

#bringing domain and password to equal length
def func(domain, password):
	for i in range(0,len(domain)-len(password)):
		password += password[i]
	return password


#((ascii value domain's char + ascii value of pass's char) mod 93 ) + 33
def passGen(domain, password):
	genPass = ''
	for i in range(0,len(domain)):
		genPass += chr(((ord(password[i]) + ord(domain[i])) % 93) + 33)
	for x in genPass:
		if (ord(x) >= 65) and (ord(x) <= 90):
			genPass += chr(ord(x)+32) + str(len(genPass))
			break
	return genPass


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", help="the domain for the password")
	parser.add_argument("-c", help="copies the generated password into your clipboard without printing it", action="store_true")
	args = parser.parse_args()

	if args.d is None:
		parser.parse_args(['-h'])
	domain = args.d
	password = getpass("Enter your bad password: ")
	

	if len(domain) > len(password):
		password = func(domain, password)
	elif len(domain) < len(password):
		domain = func(password, domain)
	else:
		pass
	

	if args.c:
		return pyperclip.copy(passGen(domain, password))
	return print("Your password:\n\n" + passGen(domain, password) + "\n")


if __name__ == '__main__':
	main()
