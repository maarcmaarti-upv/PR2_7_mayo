void on_setup() {

    const int sensor_caja = 4;
    const int sensor_paq = 5; 
    // Sensores
    pinMode(sensor_caja, INPUT_PULLUP);
    pinMode(sensor_paq, INPUT_PULLUP);

    suscribirseATopics();
    infoln("Sensores configurados en pines 4 y 5");

    // Mensaje inicial JSON
    String hello_msg = String("Hola Mundo! Desde dispositivo ") + deviceID;

    JsonDocument doc;
    doc["message"] = hello_msg;
    doc["luminosidad"] = 450;
    doc["temperatura"] = 21.5;

    String hello_msg_json;
    serializeJson(doc, hello_msg_json);

    enviarMensajePorTopic(HELLO_TOPIC, hello_msg_json);
}
