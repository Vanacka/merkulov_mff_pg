souradnice = input().split()

# Souradnice bodu A[ax, ay], B[bx, by], C[cx, cy], D[dx, dy]

ax = float(souradnice[0])
ay = float(souradnice[1])
bx = float(souradnice[2])
by = float(souradnice[3])
cx = float(souradnice[4])
cy = float(souradnice[5])
dx = float(souradnice[6])
dy = float(souradnice[7])

# Usecku AB mohu vyjadrit jako bod A + alpha*(vektor AB) podobne usecku CD -> C + beta*(vektor CD), ze soustavy
# rovnic si vyjadrime alpha a beta
a = (dx - cx)*(cy - ay) - (dy - cy)*(cx - ax)
b = (dx - cx)*(by - ay) - (dy - cy)*(bx - ax)
c = (bx - ax)*(cy - ay) - (by - ay)*(cx - ax)


if b != 0:
    alpha = a / b
    beta = c / b

# Pokud b = 0 usecky nebudou mit prusecik protoze budou rovnobezne
# Pokud a = b = 0 usecky budou lezet na stejne primce a je jeste potreba overit, zdali maji spolecnou cast
# Pokud b != 0 a a,c jsou z intervalu [0,1] znamena to ze jsou usecky ruznobezne a maji prusecik
# Pokud b != 0 a a,c > 1 nepatri do intervalu [0,1] usecky jsou ruznobezne, ale nemaji prusecik

if b == 0:
    if a == 0:
        if (max(ax, bx) >= min(cx, dx)) or (max(ay, by) >= max(cy, dy)):
            print("ANO")
        else:
            print("NE")
    else:
        print("NE")
elif alpha <= 1 and alpha >=0 and beta <= 1 and beta >=0:
    print("ANO")
else:
    print("NE")