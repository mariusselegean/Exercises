import pandas as pd
import numpy as np

brics = pd.read_csv("brics.csv", index_col=0)
print(brics)

#selectam coloana areas
#avem 3 optiuni de a selecta o coloana
print(brics['area'])
#print(brics.loc[:, "area"])
#print(brics.iloc[:, 2])


#efectuam o comparatie pe aceasta coloana si stocam rezultatul obtinut
is_huge = brics["area"] > 8

#folosim rezultatul pentru a face o selectie din df
print(brics[is_huge])


# sau se poate face intr-o singura de linie de cod


print(brics[brics["area"] >8])

result = np.logical_and((brics["area"] >8, ["brics"] <10))
print(brics(result))