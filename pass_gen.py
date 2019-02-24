#!/usr/bin/env python3

import sys

#bringing domain and password to equal length, in case domain's length is greater than the password's length --> facebook adminadm
def dBigger(domain, password):
	for i in range(0,len(domain)-len(password)):
		password += password[i]
	return password
#bringing domain and password to equal length, in case password's length is greater than the domain's length --> redditre password
def pBigger(domain, password):
	for i in range(0,len(password)-len(domain)):
		domain += domain[i]
	return domain

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
	if((len(sys.argv) < 3) or(len(sys.argv) > 3)):
		print('''
Use: python {0} [domain] [password]\n
Example: 
python {0} facebook greatpassword
4:/-=F7E@?9>-'''.format(sys.argv[0]))
		sys.exit()

	domain = sys.argv[1]
	password = sys.argv[2]
	npass = ''
	if len(domain) > len(password):
		password = dBigger(domain, password)
	elif len(domain) < len(password):
		domain = pBigger(domain, password)
	else:
		pass
	return print(passGen(domain, password))


if __name__ == '__main__':
	main()
