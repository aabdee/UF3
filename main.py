
import literales as msg

import functions as f
def main():

    f.header()
    bucle = 1
    while bucle != 0:
        nom = f.dades(msg.MSG1)
        cognom = f.dades(msg.MSG2)
        edat = f.dades(msg.MSG3)
        id = f.identificador(nom, cognom, edat)
        tecnologia = f.tecno()
        f.registres(id, nom, cognom, edat, tecnologia)
        bucle = int(input(msg.MSG8))


if __name__ == '__main__':
    main()
