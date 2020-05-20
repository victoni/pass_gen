#!/usr/bin/env python3

import sys, argparse



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
	if((len(sys.argv) < 2) or(len(sys.argv) > 2)):
		print('''
Use: python {0} [domain]\n
Example: 
python3 {0} facebook
Enter your bad password: password
Your password:

=)=?@EH6e8
'''.format(sys.argv[0]))
		sys.exit()

	domain = sys.argv[1]
	password = input("Enter your bad password: ")
	if len(domain) > len(password):
		password = func(domain, password)
	elif len(domain) < len(password):
		domain = func(password, domain)
	else:
		pass
	return print("Your password:\n\n" + passGen(domain, password) + "\n")


if __name__ == '__main__':
	main()
