import ImagenPGM as im

if __name__ == '__main__':
#   nombre = input('nombre de archivo: ')
    nombre = 'Lena_ascii.pgm'
    imagen1 = im.LeerImagen(nombre)
    imagen3 = im.Binariza(imagen1)
    im.EscribirImagen('binaria1.pgm',imagen3)
    im.Informacion(imagen1)
    im.Informacion(imagen3)
    

    
    
