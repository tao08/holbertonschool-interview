#!/usr/bin/python3
"""
0-principal
"""
isla_perímetro  =  __import__ ( '0-isla_perímetro' ). isla_perímetro

si  __nombre__  ==  "__principal__" :
    cuadrícula  = [
        [ 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 1 , 0 , 0 , 0 , 0 ],
        [ 0 , 1 , 0 , 0 , 0 , 0 ],
        [ 0 , 1 , 1 , 1 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 ]
    ]
    imprimir ( isla_perímetro ( cuadrícula ))