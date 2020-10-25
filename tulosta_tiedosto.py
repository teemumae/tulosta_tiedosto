import csv
def nayta_tulokset(tiedosto):
    tulokset = []
    with open(tiedosto, newline='') as cup:
        for rivi in cup.readlines:
            tulokset.append(rivi)
            print(tulokset)
nayta_tulokset("hemulicup.csv")
