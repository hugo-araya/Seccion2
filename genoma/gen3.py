def lectura(nombre):
    ent = open(nombre)
    cadenas = []
    vacio = ent.readline()
    for linea in ent:
        linea = linea.rstrip('\n')
        cadenas.append(linea)
    ent.close()
    return cadenas

def desorden(linea):
    acumulaDesorden = 0
    i = 0
    while i < len(linea)-1:
        carac = linea[i]
        j = i + 1
        while j < len(linea):
            if carac > linea[j]:
                acumulaDesorden = acumulaDesorden + 1
            j = j + 1
        i = i + 1
    return acumulaDesorden

def proceso(lista):
    salida = []
    for l in lista:
        d = desorden(l)
        if d < 10:
            dd = '0'+str(d)
        else:
            dd = str(d)
        salida.append(dd+l)
    salida.sort()
    return (salida)

def escritura(nombre, salida):
    sal = open(nombre, 'w')
    for elem in salida:
        sal.write(elem[2:]+'\n')
    sal.close()

if __name__ == '__main__':
    lista = lectura('adn.dat')
    salida = proceso(lista)
    escritura('adn.res', salida)
        
