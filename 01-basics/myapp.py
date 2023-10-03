while True:
    velikost_nosu = int(input("Zadejte velikost nosu: "))
    if 0 < velikost_nosu < 1000:
        break
    else:
        print("Neplatná velikost nosu. Zadejte prosím číslo v rozmezí (0, 1000).")

while True:
    jmeno = input("Zadejte své jméno: ")
    if jmeno.isalpha():
        break
    else:
        print("Neplatné jméno. Jméno může obsahovat pouze písmena, žádná čísla ani speciální znaky.")

while True:
    povolani = input("Zadejte své povolání: ")
    if jmeno.isalpha():
        break
    else:
        print("Neplatné povolání. Povolání může obsahovat pouze písmena, žádná čísla ani speciální znaky.")

print(f"Vaše jméno je {jmeno} délka vašeho nosu je {velikost_nosu} a vaše povolaní je {povolani}")

