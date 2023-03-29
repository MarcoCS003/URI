n = int(input())
def mcm(NT,DT):
    if DT == 0:
        return NT
    else:
        return mcm(DT, NT%DT)
for i in range(n):
    e = input().split()
    N1, D1, N2, D2 = int(e[0]), int(e[2]),int(e[4]), int(e[6])
    o = e[3]
    if o == '+':
        NT = (N1*D2+N2*D1)
        DT = (D1*D2)
    elif o == '-':
        NT = (N1*D2-N2*D1)
        DT = (D1*D2)
    elif o == '*':
        NT = (N1*N2)
        DT = (D1*D2)
    elif o == '/':
        NT = (N1*D2)
        DT = (D1*N2)
    print (f"{NT}/{DT} = {int(NT/mcm(NT,DT))}/{int(DT/mcm(NT,DT))}")