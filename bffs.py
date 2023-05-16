#! /usr/bin/env python3

import spacy
import re
from collections import Counter
import sys


file = sys.argv[1]

file = open(file, 'r', encoding='utf8')
book = file.read()

nlp = spacy.load('pt_core_news_md')
nlp.max_length = 1300000
av = nlp(book)

i=0
bffs = []
pessoas = []

for ent in av.ents:
        if ent[0].ent_type_ == 'PER':
            pessoas.append(ent.text)
            
print(pessoas)
if len(pessoas) > 1:
    while i<len(pessoas)-1:
        if pessoas[i]!=pessoas[i+1] and (pessoas[i],pessoas[i+1]) not in bffs and (pessoas[i+1],pessoas[i]) not in bffs:
            bffs.append((pessoas[i],pessoas[i+1]))
        elif pessoas[i]!=pessoas[i+1] and (pessoas[i],pessoas[i+1]) not in bffs:
            bffs.append((pessoas[i+1],pessoas[i]))
        elif pessoas[i]!=pessoas[i+1] and (pessoas[i+1],pessoas[i]) not in bffs:
            bffs.append((pessoas[i],pessoas[i+1]))
        i+=1
        
best_friends = Counter(bffs)
print(f'Best friends: {best_friends.most_common(10)}')
