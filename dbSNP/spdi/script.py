import re
fh = open(r"log", "r").read()
for line in fh.split("n"):
    if "}}," in line:
        print(line)
