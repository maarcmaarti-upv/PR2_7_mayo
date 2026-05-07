# PR2_entrega_7_mayo

Función: Encajado y paletizado de paquetes.

Hemos establecido la conexión vía MQTT entre 2 robots ABB antropomórficos. Uno encargado de meter 6 paquetes en una caja, y el otro encargado de paletizar las cajas una vez estas sean transportadas y cerradas.

Para ejecutar correctamente el código, se debe ejecutar el código de Arduino con la esp32s3 conectada, abrir el layout de RoboDK y dejar abiertos los scripts de MQTTListener y RobotController. Y por último ejecutar el código de MQTTListener.

El cableado de la esp32s3 es de dos botones, los dos conectados a GND y el boton que simula al sensor de presencia de los paquetes conectado por el otro lado al pin 5 y el boton de las cajas al pin 4.

Con todo esto, una vez pulsado el botón de los paquetes se inicia el programa de P&P_Paq que mueve el paquete y es introducido en la caja. Una vez se han introducido 6 paquetes, se inicia la cinta de la caja, entra en la cerradora de cajas y esta se cierra .Una vez llega al final de la cinta, se pulsa el botón de las cajas y se paletiza la caja.

En el github también se encuentran fotos tanto del layout con vista cenital cómo de el esquema eléctrico del circuito, aunque en el esquema se use un arduino UNO el cableado debe ser con la esp32s3 ya que el pinout no es igual.

Además, la parte de la entrega de GDI se encuentra en la carpeta codigos_gdi, y para que funcione se debe de crear la BD con los archivos .sql cómo hemos aprendido en las prácticas, luego ejecutar el programa de python mientras ejecutas de la forma anteriormente explicada los otros programas de RDK y Arduino.
