Extract owner, product and windows license key from Windows registry easily!

Maybe it'll be useful for red teams, ordinary people, forensics, sysadmins and others.

Run script:
```
pip3 install winregistry
py rwk.py
```
Example output:
```
λ py rwk.py
Recover Windows Key. github.com/akenov0. Enjoy!

Owner: Akenov
Product: Windows 10 Pro
Windows Key: AAAA-BBBB-CCCC-DDDD-EEE
```
You can compile it for portable use:
```
pip3 install pyinstaller
pyinstaller -F rwk.py
```
