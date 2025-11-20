import numpy as np

def MakeMatr(n, m, a, b): 
    Matr = (b-a)*np.random.random(size=(n, m)) + a
    return Matr 

def PrintMatr(Matr):
    global ans
    (nRow, nCol) = Matr.shape
    for Row in range(nRow):
        for Col in range(nCol): 
            ans += "{0: 7.3f}".format(Matr[Row][Col])
        ans += "\n"
    ans += "\n"

def ZeroCol(Matr): 
    (nRow, nCol) = Matr.shape
    st = nCol
    for Col in range(nCol):
        for Row in range(nRow):
            if Matr[Row][Col] == 0:
                st -= 1
                continue
    return st

def SortMatr(Matr): 
    (nRow, nCol) = Matr.shape
    har = []
    nom = []
    for Row in range(nRow): 
        har.append(0)
        nom.append(Row)
        for Col in range(1, nCol,2):
            if Matr[Row][Col] > 0: 
                har[Row] += Matr[Row][Col]
    for i in range(0, nRow-1):
        for j in range(i, nRow):
            if har[i] > har[j]:
                har[j],har[i] = har[j],har[i]
                nom[i],nom[j] = nom[j],nom[i]
    return nom

def CorOut(Matr, nom):
    global ans
    (nRow, nCol) = Matr.shape
    ans += "\n"
    for i in range(nRow):
        for Col in range(nCol): 
            ans += "{0: 7.3f}".format(Matr[nom[i]][Col])
        ans += "\n"

with open("Lab6_5_input.txt","r") as f:
    n,m = map(int, list(f.read().split(" ")))

ans = ""
MyMatr = MakeMatr(n, m, -10, 10)
PrintMatr(MyMatr)
col = ZeroCol(MyMatr)
ans += "There are " + str(col) + " columns with no zero elements"
ans += "\n"
nom = SortMatr(MyMatr)
CorOut(MyMatr, nom) 

with open("Lab6_5_output.txt","w+") as f:
    f.write(ans)
