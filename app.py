import csv

def capturadorData(arg):
    with open(f"{arg}", "r") as f:
        captura = csv.reader(f, delimiter=";")
        for row in captura:
            print(row)

capturadorData("./GLPISCRIPT.csv")






