import csv
def nayta_tulokset(tiedosto):
    tulokset = []
    with open(tiedosto) as cup:
        for rivi in cup:
            tulokset.append(rivi.split(','))
    #print(tulokset)
    for i in range(len(tulokset)):
        for j in range(len(tulokset[i])):
            if j == 0:
                pelaaja_1 = tulokset[i][j]
            if j == 1:
                pelaaja_2 = tulokset[i][j]
            if j == 2:
                pisteet_1 = tulokset[i][j]
            if j == 3:
                pisteet_2 = tulokset[i][j]
        print("{} {} - {} {}\n".format(pelaaja_1,pisteet_1,pisteet_2,pelaaja_2))

nayta_tulokset("hemulicup.csv")
