# Control de Motor con Raspberry Pi
Este código es un ejemplo de cómo controlar un motor con una Raspberry Pi utilizando los módulos de GPIO de Python. Se utilizan las librerías siguientes:

- time: para controlar el tiempo de espera en el código
- gpiozero: para controlar el motor
- RPi.GPIO: para configurar los pines de la Raspberry Pi
- pygame: para mostrar una interfaz gráfica
## Uso
El código define una serie de funciones que se encargan de controlar el motor (arrancar, pausa, contar), así como una interfaz gráfica (upmenu) que permite al usuario seleccionar la velocidad, el sentido de giro y el número de vueltas deseado.

## Configuración
Asegúrese de tener instaladas las librerías necesarias para ejecutar el código.

## Ejecución
Para ejecutar el código, abra una terminal en la Raspberry Pi y navegue hasta la carpeta donde se encuentra el archivo. Ejecute el código con el comando `python nombre_archivo.py`.

##  Problemas conocidos
- El código está diseñado para funcionar con una Raspberry Pi específica, por lo que es posible que deba modificar algunas líneas de código para adaptarlo a su configuración.
- Si el código no funciona correctamente, asegúrese de haber configurado los pines correctamente.
## Créditos
Este código fue creado utilizando información de los siguientes recursos:

- [gpiozero documentation](https://gpiozero.readthedocs.io/en/stable/)
- [RPi.GPIO documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
## Licencia
Este código está disponible bajo la licencia MIT. Puede ser utilizado, modificado y distribuido libremente siempre y cuando se incluya este aviso de licencia.