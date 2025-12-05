import hashlib

s="iwrupvqb"
i=0
while True:
    h=hashlib.md5(f"{s}{i}".encode())
    if h.hexdigest()[:6]=="0"*6:break
    i+=1
print(i)
