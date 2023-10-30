# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install googlesearch-python

from googlesearch import search

# Términos de búsqueda
query = "Python programming"

# Realiza una búsqueda en Google en línea
for result in search(query, num=5, stop=5, pause=2):
    print(result)
