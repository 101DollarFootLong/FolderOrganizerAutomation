import re
f = "hello (1).png"
if re.search("\(\d+\)", f):
    print("yes")