casos = 1 
while True:
    n = input().split()
    n1 = int(n[0])
    q = int(n[1])
    if n1 == 0:
        break
    canicas = []
    print(f"CASE# {casos}:")
    for i in range(n1):
        canicas.append(int(input()))   
    canicas.sort()               
    for j in range(q):
        valor = int(input())
        final = len(canicas) -1
        inicio = 0
        while (inicio <= final):
            puntero = (inicio + final) //2
            if canicas[puntero] == valor:
                while (canicas[puntero] == valor):
                    puntero -= 1
                else:
                    print(f"{valor} found at {puntero +2}")
                    break
            elif valor > canicas[puntero]:
                inicio = puntero +1
            else:
                final = puntero -1
            puntero = 0
        else:
            print(f"{valor} not found")
    casos += 1