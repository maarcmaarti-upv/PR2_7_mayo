uint8_t ledStatus = 0;
// Aquí no hemos tocado nada ya que sólo usamos el MQTT para enviar mensajes a los topics dependiendo de los inputs que recibe la esp32s3
void setInternalLed(uint8_t status) {
  if ( ledStatus == status ) // Nothing to do
    return;
    
  ledStatus = status;
  if ( status ) {
    infoln("Led: on");
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    infoln("Led: off");
    digitalWrite(LED_BUILTIN, LOW);
  }

  // TODO: Deberíamos publicar el estado del dispositivo cada vez que cambie
}


