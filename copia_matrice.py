
def crea_matrice(N):
    matrice = []
    for i in range(0, N):
        matrice.append([])
        for j in range(0, N):
            matrice[i].append(j)
            matrice[i][j] = 0
    for i in range(0, N):
        for j in range(0, N):
            matrice[i][j] = "-"
    for l in matrice:
        print(l)
    return 0