#!/usr/bin/env python3

def manejarSioNo(mensaje):
    terminar = ''
    while (terminar.lower() != 's' and terminar.lower() != 'n'):  # Garantiza que se introduzca 'Si' o 'No'
            terminar = input(mensaje).lower()
    return terminar
    
def datosReferenciarSitioWeb():
    try:
        nombreAutor = input('Nombre del autor: ')
        fechaPublicacion = input('Fecha de publicacion: ')
        tituloArticulo = input('Título del artículo: ')
        nombreSitioWeb = input('Nombre del sitio web: ')
        urlSitioWeb = input('URL del sitio web:')
        return (nombreAutor, fechaPublicacion, tituloArticulo, nombreSitioWeb, urlSitioWeb)
    except KeyboardInterrupt:
        return manejarSioNo('\nDesea terminar el programa? (s/N): ')    
    except:
        raise 'Ocurrio un error desconocido ;v'


# Formato sitio web en APA:
# <NombreAutor>, (<fecha publicación>). <Titulo del Artículo>. <Nombre del sitio web>. Disponible en <URLsitioWeb>
def referenciarSitioWeb():
    print('''\nEsta aplicacion permite referenciar sitios web empleando normas APA.  
    Las citas en dicho formato apareceran en un archivo llamado 'referencias.txt'\n''')

    #datos = datosReferenciarSitioWeb()
    #while datos != 's':
    endFlag = 'CONTINUE'
    while(endFlag != 'END'):
        datos = datosReferenciarSitioWeb()
        if type(datos) == tuple: 
            # Escribir en el archivo las referencias
                with open("referencias.txt", "a") as referencias:
                    referencias.write(f'{datos[0]}, ({datos[1]}). {datos[2]}. {datos[3]}. Disponible en: {datos[4]}.\n')
                    continuar = manejarSioNo('Desea Continuar adicionando referencias? (s/N): ')
                    if continuar == 'n':
                        endFlag = 'END'
                        print('Referencias escritas exitosamente. Saliendo del programa...')
                    



        
referenciarSitioWeb()