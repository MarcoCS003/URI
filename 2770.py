while True:
    try:
        x1, y1, rango = [int(i) for i in input().split()]
        for i in range(rango):
            x2, y2 = [int(i) for i in input().split()]
            if x2 <= x1 and y2<=y1 or x2 <= y1 and y2<= x1 :
                print("Sim")              
            else:
                print("Nao")
    except EOFError:
        break