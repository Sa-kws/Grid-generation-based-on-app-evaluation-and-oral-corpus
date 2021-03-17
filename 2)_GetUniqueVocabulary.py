from collections import OrderedDict
import re

name_of_file = 'Wiki_Fleur.txt'

# version 1 - sortie : une grande liste
donnees = ''
with open(, name_of_file, 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        donnees += re.sub(r'[^\w\s]', '', ligne.lower().replace('\n', ' '))
cleaned = list(OrderedDict.fromkeys(donnees.split(' ')))
print(cleaned)


# Version 2 - sortie : une liste par ligne
donnees = [ligne.lower().replace('\n', ' ') for ligne in open(name_of_file, 'r', encoding='utf-8')]
donnees = [re.sub(r'[^\w\s]', '', x).split(' ') for x in donnees]
cleaned = [list(OrderedDict.fromkeys(x)) for x in donnees]
print(cleaned)
