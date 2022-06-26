import os
from winregistry import WinRegistry

""" RWK - Recover Windows Key """
""" github.com/akenov0 """

client = WinRegistry()

kpath = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion"

""" get data """
owner = client.read_entry(kpath, "RegisteredOwner")
product = client.read_entry(kpath, "ProductName")
key1 = os.popen("wmic path softwarelicensingservice get OA3xOriginalProductKey").read().split("\n")  # powerful oneline

""" print data """
print("Recover Windows Key. github.com/akenov0. Enjoy!\n")
print(f"Owner: {owner.value}")
print(f"Product: {product.value}")
print(f"Windows Key: {key1[2]}")

""" Happy Using. This is rewrite of my old project "GWLK" i wrote at end of 2021. You won't find it, because i deleted repo. """
""" P.S. Please subscribe to t.me/neverspace """