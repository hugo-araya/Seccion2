im = open('Image/Lena_ascii.pgm')
magica = im.readline().rstrip('\n')
comentario = []
linea = im.readline().rstrip('\n')
while linea[0] == '#':
    comentario.append(linea)
    linea = im.readline().rstrip('\n')
dimension = linea.split(' ')
ancho = int(dimension[0])
if dimension[1] == '':
    alto = int(dimension[2])
else:
    alto = int(dimension[1])

grises = int(im.readline().rstrip('\n'))
pixeles = []
for linea in im:
    linea = linea.rstrip('\n')
    lista = linea.split(' ')
    for elem in lista:
        if elem != '':
            pixeles.append(int(elem))
print(len(pixeles))

nueva = []
for pixel in pixeles:
    nueva.append(grises-pixel)

sal = open('Image/lena_ByN_3.pgm', 'w')
sal.write('P2\n')
sal.write('# Creada por Hugo Araya Carrasco\n')
sal.write('512 512\n')
sal.write('255\n')
for pixel in nueva:
    sal.write(str(pixel)+' ')
sal.write('\n')
im.close()
sal.close()

