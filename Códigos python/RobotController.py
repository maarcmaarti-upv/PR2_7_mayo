from robodk import robolink

# Conexión con RoboDK
RDK = robolink.Robolink()

# Contador de paquetes
contador_paq_robot = 0


def handle_message(mqttc, topic, payload):
    global contador_paq_robot

    payload = payload.strip().lower()

    # -------------------------
    # EVENTO PAQUETE
    # -------------------------
    if topic == "pr2/sahuquillers/paq" and payload == "paquete":

        contador_paq_robot += 1

        ejecutar_pp_paq()

        # Cada 6 paquetes ejecuta cajas
        if contador_paq_robot == 2:
            ejecutar_cajas()
            contador_paq_robot = 0

    # -------------------------
    # EVENTO CAJA
    # -------------------------
    elif topic == "pr2/sahuquillers/caja" and payload == "caja":
        print("→ Evento caja recibido")
        ejecutar_paletizado()


# -------------------------
# PROGRAMAS ROBO DK
# -------------------------

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
