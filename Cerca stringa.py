file = open("file.txt", "r")
contatore = 0
lista = []
cerca = input("Inserisci la parola o lettera che stai cercando: ")
for line in file:
    for parole in line.split():
        lista.append(parole)

contatore = lista.count(cerca)

print("La parola/lettera che hai inserita è stata trovata", contatore, "volte")

file.close()