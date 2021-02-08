import csv
import sys, os

def nacti_soubor(jmeno_souboru):
    """ Načte vstupní soubor se souřadnicemi bodů a ošetří nekorektní vstupy (parametr je název souboru) """
    try:
        with open(os.path.join(sys.path[0], jmeno_souboru+".txt"), 'r', encoding="UTF-8") as f:
            reader = csv.reader(f)
            x_list = []
            y_list = []
            
            # ? První číslo přiřadí seznamu X součadnic, druhé seznamu Y souřadnic
            for c, (x, y) in enumerate(reader):
                x_list.append(int(x))
                y_list.append(int(y))

            # ? Zkontroluje, zda jsou souřadnice úplné
            if len(x_list) != len(y_list):
                print("Součadnice bodů jsou chybné. Zkontrolujte prosím vstupní soubor.")
                quit()
            elif not x_list or not y_list:
                print("Souřadnice bodů jsou chybné. Zkontrolujte prosím vstupní soubor.")
                quit()
            elif len(x_list) <= 2:
                print("Polygon musí tvořit alespoň 2 body.")
                quit()
            else:
                print("Polygon je tvořen", len(x_list), "body.")

    except PermissionError:
        print(f'K souboru "{jmeno_souboru}.txt" nemá program přístup.')
        exit()
    except FileNotFoundError:
        print(f'Soubor "{jmeno_souboru}.txt" nebyl nenalezen.')
        exit()
    except ValueError:
        print(f'Soubor "{jmeno_souboru}.txt" je chybný - obsahuje chybnou hodnotu.')
        exit()
    return x_list, y_list


def uloz_soubor(s):
    """ Uloží souřadnice do textového souboru """

    try:
        file = open(os.path.join(sys.path[0], "export.txt"), 'w', encoding="UTF-8")
        file.write("Souřadnice těžnice jsou: {}".format(s))
        file.close()
    except PermissionError:
        print(f'K adresáři není přístup.')
        exit()

def teznice(x_l, y_l):
    """ Vypočtě težnici polygonu na základě seznamů bodů, který jej tvoří. """

    l = len(x_list)
    x = sum(x_list) / l
    y = sum(y_list) / l
    return(x, y)

# ? Načte vstupní data
body = nacti_soubor("data")

# ? uloží souřadnicové seznamy
x_list = body[0]
y_list = body[1]

souradnice = teznice(x_list, y_list)
uloz_soubor(souradnice)
print("Těžnice má souřadnice:", souradnice)
