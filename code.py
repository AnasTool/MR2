import os, sys
os.system("git pull")
try:
    __import__("anas_enc").anas()
except Exception as e:
    exit(str(e))