# Password Generator
Small script that generates a password that satisfies the conditions (uppercase letters, lowercase letters, symbols, numbers) based on an easier, universal one.

```
usage: pass_gen.py [-h] [-d D] [-c]

optional arguments:
  -h, --help  show this help message and exit
  -d D        the domain for the password
  -c          copies the generated password into your clipboard without printing it
```

Examples:
``` 
$ python3 pass_gen.py -d yahoo
Your bad password: password
Your password:

P)BIMO:3p8

```
```
$ python3 pass_gen.py -d yahoo -c
Your bad password: [typing]
$ #copied into your clipboard
```

`password` can be cracked instantly using wordlists.
`P)BIMO:3p8` can be cracked in 53 years (tested [here](https://howsecureismypassword.net/))
