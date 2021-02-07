import sys, os

def nacti_soubor(jmeno_souboru):
    """ Načte soubor typu txt a ošetří nekorektní vstupy. """
    try:
        file = open(os.path.join(sys.path[0], jmeno_souboru+".txt"), 'r', encoding="UTF-8")
        text = file.read()

    except PermissionError:
        print(f'K souboru "{jmeno_souboru}.txt" nemá program přístup.')
        exit()
    except FileNotFoundError:
        print(f'Soubor "{jmeno_souboru}.txt" nebyl nenalezen.')
        exit()
    except ValueError:
        print(f'Soubor "{jmeno_souboru}.txt" je chybný.')
        exit()
    return text

def uloz_soubor(samo, sou):
    """ Uloží slovníky samohlásek a souhlásek do souboru letters.txt """

    try:
        file = open(os.path.join(sys.path[0], "export.txt"), 'w', encoding="UTF-8")
        file.write("Samohlásky: {} \nSouhlásky: {}".format(samo, sou))
        file.close()
    except PermissionError:
        print(f'K adresáři není přístup.')
        exit()


def letters(txt):
    """ Vytvoří slovník samohlásek, kde klíčem je název samohlásky a hodnotou její počet. """

    # ? Definování hledaných samohlásek a souhlásek
    samo = ["a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"]
    sou = ["h", "ch", "k", "r", "d", "t", "n", "ž", "š", "c", "č", "ř", "j", "ď", "ť", "ň", "b", "f", "l", "m", "p", "s", "v", "z"]
    # ? Založení vystupujících slovníků
    sou_dic = {}
    samo_dic = {}

    # ? zkontroluje text znak po znaku
    for index in range(len(txt)):
        # ? hledá samohlásky
        for i in range(len(samo)):
            # ? hledá souhlásky
            for a in range(len(sou)):
                if txt[index] == samo[i]:
                    # ? pokud ve slovníku již je, přičte 1
                    if samo[i] in samo_dic:
                        samo_dic[samo[i]] += 1
                    # ? pokud ve slovníku ještě není, zaliží jej
                    else:
                        samo_dic[samo[i]] = 1
                elif txt[index] == sou[a]:
                    if sou[a] in sou_dic:
                        sou_dic[sou[a]] += 1
                    else:
                        sou_dic[sou[a]] = 1
    return samo_dic, sou_dic

# ? Načte soubor do proměnné text a převede na malá písmena
text = nacti_soubor("data").lower()
# ? Ochrana proti práznému vstupnímu souboru
if not text:
    print("Vstupní soubor je prázdný, zkontrolujte jej prosím.")
    quit()
else:
    print("Text byl načten v pořádku (obsahuje", len(text), 'znaků).')
    uloz_soubor(letters(text)[0], letters(text)[1])
    print('Samohlásky a souhlásky naleznete v souboru "export.txt"')
