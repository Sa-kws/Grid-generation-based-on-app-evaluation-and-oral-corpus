### IN_DATAS:
- IN_DATAS doit être créé et rempli avec le répertoire ('ESLO-2021-03-08') avant la première execution. 
- Les répertoires ESLO_ISO et ESLO_UTF-8 peuvent être créés au préalable, mais ce n'est pas nécessaires, en revanche, ils doivent être vide avant la première execution

### OUT_DATAS:
- OUT_DATAS peut-être créé au préalable mais non nécessaire
- Tous les fichiers de sorties seront stockés dans ce répertoire

### Ordre d'execution:
1. 1)_SortESLOEncoding_preprocess.py
2. 2)_FixTranscriptions_ISO_preprocess.py
3. 2)_FixTranscriptions_UTF-8_preprocess.py
4. 3)_GetChildLocucteurs_extract.py
5. 4)_GetESLOTextTranscriptions_ISO_extract.py
6. 4)_GetESLOTextTranscriptions_UTF-8_extract.py
7. 5)_GetChildTranscriptions_ISO_extract.py
8. 5)_GetChildTranscriptions_UTF-8_extract.py
9. 6)_GetLemmaOrPosFrequency_extract.py
10. 6)_GetLemmaOrPosFrequencyByESLO_extract.py
11. 7)_GetLemmaOrPosFrequencyChild_extract.py
12. 8)_GetPercentage_calculate.py 

*Se réferer au fichier 'Script_execution_order.tsv' pour plus de détails sur l'execution des scripts*
