from math import *

def crea_matrice(matrice):
    for i in range(0, N):
        matrice.append([])
        for j in range(0, N):
            matrice[i].append(j)
            matrice[i][j] = 0

def posiziona_asterischi(pos_x1, pos_x2, pos_y1, pos_y2):
    for i in range(0, N):
        for j in range(0, N):
            if i == pos_x1 - 1 and j == pos_y1 - 1:
                matrice[i][j] = "*"
                pos_x1 = i
                pos_y1 = j
            elif i == pos_x2 - 1 and j == pos_y2 - 1:
                matrice[i][j] = "*"
                pos_x2 = i
                pos_y2 = j
            else:
                matrice[i][j] = "-"

def stampa_matrice(matrice):
    for l in matrice:
        print(l)

def calcola_distanza(pos_x1, pos_x2, pos_y1, pos_y2):
    distanza = pow(pos_x2 - pos_x1, 2) + pow(pos_y2 - pos_y1, 2)
    distanza = sqrt(distanza)
    return distanza

N = int(input("Inserisci il valore N: "))
matrice = []

crea_matrice(matrice)

pos_x1 = int(input(f"Inserisci la riga tra 1 e {N} del primo asterisco: "))
if pos_x1 > N or pos_x1 == 0:
    while pos_x1 > N or pos_x1 == 0:
        pos_x1 = int(input("Inserisci un valore valido: "))
pos_y1 = int(input(f"Inserisci la colonna tra 1 e {N} del primo asterisco: "))
if pos_y1 > N or pos_y1 == 0:
    while pos_y1 > N or pos_y1 == 0:
        pos_y1 = int(input("Inserisci un valore valido: "))
pos_x2 = int(input(f"Inserisci la riga tra 1 e {N} del secondo asterisco: "))
if pos_x2 > N or pos_x2 == 0:
    while pos_x2 > N or pos_x2 == 0:
        pos_x2 = int(input("Inserisci un valore valido: "))
pos_y2 = int(input(f"Inserisci la colonna tra 1 e {N} del secondo asterisco: "))
if pos_y2 > N or pos_y2 == 0:
    while pos_y2 > N or pos_y2 == 0:
        pos_y2 = int(input("Inserisci un valore valido: "))

posiziona_asterischi(pos_x1, pos_x2, pos_y1, pos_y2)
stampa_matrice(matrice)
print(int(calcola_distanza(pos_x1, pos_x2, pos_y1, pos_y2)))
