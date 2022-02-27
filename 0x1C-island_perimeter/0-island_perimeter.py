#!/usr/bin/python3

""" Función para encontrar el perímetro de una isla """


def  island_perimeter ( cuadrícula ):
    """
    Entrada: Lista de listas
    Devoluciones: Perímetro de la isla
    """
    cuenta  =  0
    fila  =  len ( cuadrícula )
    col  =  len ( cuadrícula [ 0 ]) si  fila  más  0

    para  i  en el  rango ( len ( cuadrícula )):
        para  j  en el  rango ( len ( cuadrícula [ i ])):

            idx  = [( yo  -  1 , j ), ( yo , j  -  1 ), ( yo , j  +  1 ), ( yo  +  1 , j )]
            comprobar  = [ 1  si  k [ 0 ] en el  rango ( fila ) y  k [ 1 ] en el  rango ( columna ) si no  0
                     para  k  en  idx ]

            si  cuadrícula [ i ][ j ]:
                cuenta  +=  suma ([ 1  si  no es  r  o  no es  cuadrícula [ k [ 0 ]][ k [ 1 ]] sino  0
                              para  r , k  en  zip ( cheque , idx )])

    volver ( contar )