import csv
import sys, os

def nacti_soubor(jmeno_souboru):
    """ Načte vstupní soubor se souřadnicemi bodů a ošetří nekorektní vstupy (parametr je název souboru) """
    try:
        with open(os.path.join(sys.path[0], jmeno_souboru+".txt"), 'r', encoding="UTF-8") as f:
            reader = csv.reader(f)

    except PermissionError:
        print(f'K souboru "{jmeno_souboru}.txt" nemá program přístup.')
        exit()
    except FileNotFoundError:
        print(f'Soubor "{jmeno_souboru}.txt" nebyl nenalezen.')
        exit()
    except ValueError:
        print(f'Soubor "{jmeno_souboru}.txt" je chybný.')
        exit()
    return reader


print(nacti_soubor("data"))



