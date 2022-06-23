from advancedRemote import AdvancedRemote
from device import Device
from radio import Radio
from tv import Tv
from smartTv import SmartTv
from datetime import datetime
import time


# RODOLFO BACILIO CHIVALAN DE LEON     1561817
# DIEGO ANDRES VELIZ                   1230019


def main():
    aparato: Device
    nivel = None
    run: bool = True
    while run:
        aparato = aparatos()
        if aparato is None:
            print('No ha seleccionado nada, cerrando el programa...')
            run = False
        else:
            control: AdvancedRemote = AdvancedRemote(aparato)
            controles(control)
            print(f'Regresando')


def aparatos() -> [Device | None]:
    option: int = 0
    while option != 4:
        print("-".center(55, "-") + '|')
        print('\nMenu')
        print('\nEscoja un Control')
        print('1- Tv')
        print('2- Smart Tv')
        print('3- Radio')
        print('4- Cerrar')
        print("-".center(55, "-") + '|')
        option = int(input('Ingrese una opción: '))
        if option == 1:
            print(f'Ha elegido Tv')
            return Tv()
        elif option == 2:
            print(f'Ha elegido Smart Tv')
            return SmartTv()
        elif option == 3:
            print(f'Ha elegido Radio')
            return Radio()
        elif option == 4:
            print(f'Regresando')
            return None
        else:
            print('Ingrese una opcion correcta')
            continue


def controles(control: AdvancedRemote):
    option: int = 0
    while option != 7:
        print("-".center(55, "-") + '|')
        print('\nMenu')
        print('\nEscoja un accion')
        print('1- Boton de Encendido')
        print('2- Subir Volumen')
        print('3- Bajar Volumen')
        print('4- Mute')
        print('5- Cambiar canal (Hacia arriba)')
        print('6- Cambiar canal (Hacia abajo)')
        print('7- Terminar comandos')
        print("-".center(55, "-") + '|')
        option = int(input('Ingrese una opción: '))
        if option == 1:
            print(f'Ha elegido Boton de Encendido')
            control.toggle_power()
        elif option == 2:
            print(f'Ha elegido Subir Volumen')
            control.volume_up()
        elif option == 3:
            print(f'Ha elegido  Bajar Volumen')
            control.volume_down()
        elif option == 4:
            print(f'Ha elegido Mute')
            control.mute()
        elif option == 5:
            print(f'Ha elegido  Cambiar canal (Hacia arriba)')
            control.channel_up()
        elif option == 6:
            print(f'Ha elegido  Cambiar canal (Hacia abajo)')
            control.channel_down()
        elif option == 7:
            print(f'Regresando')
        else:
            print('Ingrese una opcion correcta')
            continue


main()
