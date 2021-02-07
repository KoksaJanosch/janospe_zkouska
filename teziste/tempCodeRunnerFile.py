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
