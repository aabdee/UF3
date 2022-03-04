import literales as msg
import csv

def dades(msg):
    dada = input(msg)
    return dada

def identificador(n, s, a):
    n_upper= n.upper()
    s_upper= s.upper()
    id =  (n_upper[0:2] + '-' + s_upper[-2:] + '-' + str(a))
    return id

def tecno():
    x = int(input(msg.MSG4))
    match x:
        case 1:
            tec= msg.MSG5
        case 2:
            tec =msg.MSG6
        case _:
            print(msg.MSG7)
    return tec

def header():
    with open('files/archivo.csv', 'a') as csvfile:
        writecsv = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writecsv.writerow(['ID', 'Nom', 'Cognom', 'Edat', 'Tecnologia'])

def registres(id, nom, cognom, edat, tecnologia):
    with open('files/archivo.csv', 'a+') as csvfile:
        writecsv = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writecsv.writerow([id, nom, cognom, edat, tecnologia])