def max(num1, num2, num3):
    if(num1>num2 and num1>num3):
        max=num1
    elif(num2>num1 and num2>num3):
        max=num2
    else:
        max=num3
    return max

num1 = input("Inserisci il primo numero: ")
num2 = input("Inserisci il secondo numero: ")
num3 = input("Inserisci il terzo numero: ")
num_max = max(num1, num2, num3)
print("Il numero maggiore tra i 3 è: ", num_max)