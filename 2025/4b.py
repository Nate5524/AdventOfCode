g = []
with open("4.txt", "r") as file:
    g = [l.strip() for l in file]
dg = [list(s) for s in g]

R = len(g)
C = len(g[0])

def adj_ct(r:int,c:int)->int:
    t = 0
    for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        nr=dr+r
        nc=dc+c
        t += int(0<=nr<R and 0<=nc<C and g[nr][nc]=="@")
    return t

a=0
pa=None
while pa!=a:
    pa=a
    for r in range(R):
        for c in range(C):
            if g[r][c]=="@" and adj_ct(r,c) < 4:
                dg[r][c]="x"
                a+=1
    # print("\n".join(map(lambda x: "".join(x), dg)))
    g=[x.copy() for x in dg]
print(a)