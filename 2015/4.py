import hashlib

s="iwrupvqb"
i=0
while True:
    h=hashlib.md5(f"{s}{i}".encode())
    if h.hexdigest()[:5]=="00000":break
    i+=1
print(i)
