# Clicker
Movimiento automatizado de raton. Por defecto, sin parametro se seleccionan 2 coordeandas aleatorias, durante 3 segundos.

## Atributos
**-m**: realizas tu las coordenadas. Sin argumento.  
**-t**: modificar el tiempo entre movimiento. Defecto: 3 segundos. Numero.  
**-p**: numero de coordenadas que se generaran. Numero.  
**-f**: lee configuration.txt. Sin argumento.  
**-h**: comando de ayuda.  

## Ejemplos
Ejecucción simple con 2 coordenadas creadas aleatorias, cada 3 segundos movimiento.  
`python clicker.py`  
Ejecucción 5 coordenadas creadas aleatorias, cada 2 segundos moviento.  
`python clicker.py -p 5 -t 2`  
Ejecucción 2 coordenadas seleccionadas por ti, cada 3 segundos moviento.  
`python clicker.py -m`  
Ejecucción almacenada en el archivo *configuracion.txt*  
`python clicker.py -f`  