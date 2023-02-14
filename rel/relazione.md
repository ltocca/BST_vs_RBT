---
author:
- Leonardo Toccafondi   
date: February 14, 2022
title: Alberi binari di ricerca e alberi rosso-neri
---

# Introduzione

In questa relazione si andranno a confrontare alberi binari di ricerca e alberi rosso-neri, al fine di determinare le differenze, e di conseguenza i loro vantaggi e svantaggi, tra queste due strutture dati

# Descrizione

Un albero è una struttura dati composta da elementi, detti nodi: ognuno contiene una chiave che lo identifica univocamente. Inoltre, può contenere anche altri campi, come ad esempio un puntatore ai nodi *figli*. Il nodo dal quale discendono tutti gli altri nodi viene detto *radice* (in inglese root). Un nodo che non possiede figli è detto *foglia*. Viene definito *cammino* da un nodo un nodo n ad un nodo m una sequenza di nodi connessi da archi che portano da n ad m. La *lunghezza del cammino* è pari al numero di nodi che si incontrano nel cammino, escluso il primo. Di conseguenza la lunghezza di un cammino contenente un solo nodo è pari a 0. Si dice *altezza* $h$ dell’albero la lunghezza
massima tra i cammini che uniscono la radice alla foglie.

Si parla di albero binario quando ogni nodo ha al massimo due figli: si
indicano come figlio sinistro e destro.