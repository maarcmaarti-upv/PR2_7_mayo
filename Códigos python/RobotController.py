from robodk import robolink

# Conexión con RoboDK
RDK = robolink.Robolink()

# Contador de paquetes
contador_paq_robot = 0


def handle_message(mqttc, topic, payload):
    global contador_paq_robot

    payload = payload.strip().lower()

    # Cuando recibe en el topic "pr2/sahuquillers/paq" -> "paquete"
    if topic == "pr2/sahuquillers/paq" and payload == "paquete":

        contador_paq_robot += 1

        ejecutar_pp_paq()

        # Cada 6 paquetes ejecuta cajas
        if contador_paq_robot == 6:
            ejecutar_cajas()
            contador_paq_robot = 0

    # Cuando recibe en el topic "pr2/sahuquillers/caja" -> "caja"
    elif topic == "pr2/sahuquillers/caja" and payload == "caja":
        print("→ Evento caja recibido")
        ejecutar_paletizado()


# Programas de RoboDK
def ejecutar_pp_paq():
    programa = RDK.Item("P&P_Paq", robolink.ITEM_TYPE_PROGRAM)

    if programa.Valid():
        if not programa.Busy():   # evita solapamientos
            programa.RunProgram()
        else:
            print("Programa P&P_Paq ocupado")
    else:
        print("ERROR: No se encontró el programa P&P_Paq en la estación.")


def ejecutar_paletizado():
    programa = RDK.Item("P&P_CajaCerrada")

    if programa.Valid():
        if not programa.Busy():   # evita solapamientos
            programa.RunProgram()
        else:
            print("Programa P&P_CajaCerrada ocupado")
    else:
        print("ERROR: No se encontró el programa P&P_CajaCerrada en la estación.")
              
def ejecutar_cajas():
    programa = RDK.Item("Cajas", robolink.ITEM_TYPE_PROGRAM)

    if programa.Valid():
        if not programa.Busy():   # evita solapamientos
            programa.RunProgram()
        else:
            print("Programa Cajas ocupado")
    else:
        print("ERROR: No se encontró el programa P&P_CajaCerrada en la estación.")
