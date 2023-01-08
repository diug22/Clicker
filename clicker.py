
import sys
import os
from pynput.mouse import Button, Controller,Listener
import time
import random
import json
import copy
from types import SimpleNamespace as Namespace


mouse = Controller()

class Configuration:
    
    def __init__(self):
        self.sleep_time = 3
        self.coordenadas = []
        self.manual_displayed = False
        self.positions = 2
        self.file = False

    def write_configuration(self):
        if (os.path.exists("configuracion.txt")):
            os.remove("configuracion.txt")
        f = open("configuracion.txt", "w")
        f.write(json.dumps(self.__dict__))
        f.close()   
        
    def print_configuration(self):
        print('--------------- \nConfiguracion. \nManual displayed: {0} \nPositions {1} \nSleep Time: {2} \nCoordenadas: {3} \n--------------- \n'
              .format(self.manual_displayed,self.positions,self.sleep_time,self.coordenadas))

        

configuration = Configuration() 
def on_click(x, y, button, pressed):
    if pressed:
        configuration.coordenadas.append((x, y))
    if not pressed:
        # Stop listener
        return False



def helpCommand():
    print('Automatizacion de movimientos de raton. Por defecto realiza un movimiento cada 3 segundos a 2 posiciones.')
    print('-m: realizas tu las coordenadas. Sin argumento.')
    print('-t: modificar el tiempo entre movimiento. Defecto: 3 segundos. Numero.')
    print('-p: numero de coordenadas que se generaran. Numero.')
    print('-f: lee configuration.txt')
    
def checkArg(arg):
    try:
        arg = int(arg)
    except:
        print('Algun argumento no es correcto!')
        


    
def classArg(index,args):

    if args[index] == '-t':
        checkArg(args[index+1])
        configuration.sleep_time = int(args[index+1])
    if args[index] == '-p':
        checkArg(args[index+1])
        configuration.positions = int(args[index+1])
    if args[index] == '-m':
        configuration.manual_displayed = True
        index -= 1
    if args[index] == '-h':
        helpCommand()
        sys.exit()
    if args[index] == '-f':
        configuration.file = True
        index -= 1
    index += 2
    return index

def manual_configuration():
    print('Haz click en {0} posiciones de tu pantalla. Almacenadas {1}'.format(configuration.positions,len(configuration.coordenadas)))
    with Listener(
        on_click=on_click) as listener:
            listener.join()
    listener.stop()
    
def random_configuration():
    x = random.randrange(400, 500, 2)   
    y = random.randrange(400, 500, 2) 
    configuration.coordenadas.append((x, y))
    
def read_configuration():
    try:
        f = open("configuracion.txt", "r")
        json_file = f.read()
        c = json.loads(json_file, object_hook=lambda d: Namespace(**d))
        return copy.copy(c)       
    except:
        print('No existe el fichero  "configuracion.txt"')
        sys.exit()
 
def adjust_configuration(conf,copy_conf):
        conf.sleep_time = copy_conf.sleep_time
        conf.coordenadas = copy.copy(copy_conf.coordenadas)
        conf.manual_displayed = copy_conf.manual_displayed
        conf.positions = copy_conf.positions
        conf.file = copy_conf.file

if __name__ == "__main__":
    
    n = len(sys.argv)
    arg = 1
    while arg < len(sys.argv):
        arg = classArg(arg,sys.argv)
    
    if configuration.file:
        copy_configuration = read_configuration()
        adjust_configuration(configuration,copy_configuration)
    
    while len(configuration.coordenadas) < configuration.positions and not configuration.file:
        if configuration.manual_displayed:
            manual_configuration()
        else:
            random_configuration()
    configuration.manual_displayed = False
    
    configuration.print_configuration()
    configuration.write_configuration()
        
    print('Comenzamos, ahora disfrute.')
    index = 0
    while True:
        try:
            configuration.coordenadas[index]
        except:
            index = 0
        mouse.position = configuration.coordenadas[index]
        index += 1
        time.sleep(configuration.sleep_time)
        