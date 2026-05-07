import psycopg
import paho.mqtt.client as mqtt
import uuid

# Configuración de MQTT
broker = "mqtt.dsic.upv.es"
port = 1883
user = "giirob"
passwd = "UPV2024"

# Topics
TOPIC_PAQ = "pr2/sahuquillers/paq"
TOPIC_CAJA = "pr2/sahuquillers/caja"

# Configuracion de la BD
DB_CONFIG = {
    "dbname": "proyecto",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# Estado general
contador_paq = 0
contador_caja = 0
ultimo_pallet = None

# Funciones de la BD
def get_conn():
    return psycopg.connect(**DB_CONFIG)

# Crea nuevo pallet en la BD
def crear_pallet():
    global ultimo_pallet

    codigo = str(uuid.uuid4())[:8]

    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO pallet (codigo, tamano, material) VALUES (%s, %s, %s)",
                    (codigo, 100.0, "madera")
                )
                conn.commit()

        ultimo_pallet = codigo
        print(f"[DB] Pallet creado: {codigo}")

    except Exception as e:
        print("Error creando pallet:", e)

# Crea nueva caja en la BD
def crear_caja():
    global ultimo_pallet

    # Si no hay pallet, creamos uno primero
    if ultimo_pallet is None:
        crear_pallet()

    codigo = str(uuid.uuid4())[:8]

    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO caja (codigo, tamano, material, codigo_pallet)
                       VALUES (%s, %s, %s, %s)""",
                    (codigo, 10.0, "carton", ultimo_pallet)
                )
                conn.commit()

        print(f"[DB] Caja creada: {codigo} → pallet {ultimo_pallet}")

    except Exception as e:
        print("Error creando caja:", e)

# MQTT callback
def on_message(client, userdata, msg):
    global contador_paq, contador_caja

    topic = msg.topic
    payload = msg.payload.decode("utf-8")

    print(f"[MQTT] {topic}: {payload}")

    # Paquetes → Cajas
    if topic == TOPIC_PAQ:
        contador_paq += 1

        if contador_paq >= 6:
            crear_caja()
            contador_paq = 0

    # Cajas → Pallets
    elif topic == TOPIC_CAJA:
        contador_caja += 1

        if contador_caja >= 12:
            crear_pallet()
            contador_caja = 0

# Main
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(user, passwd)

client.on_message = on_message

client.connect(broker, port, 60)

client.subscribe("pr2/sahuquillers/#", 0)

print("Escuchando MQTT...")
client.loop_forever()
