import time
from robodk import robolink, robomath

RDK = robolink.Robolink()

CajaBase = RDK.Item('CajaAbierta')
SistRefCinta = RDK.Item('FPaq')

DESPLAZAMIENTO_MM = 700
TIEMPO_TOTAL = 1.5
PASOS = 60

# 🔥 Espera de 36 segundos ANTES de iniciar el ciclo
time.sleep(5)

if CajaBase.Valid() and SistRefCinta.Valid():

    # 1. Crear copia
    CajaBase.Copy()
    Caja = RDK.Paste(SistRefCinta)

    if not Caja.Valid():
        raise Exception("No se pudo crear la copia de la caja.")

    Caja.setName('Caja_Movil')

    pose_ini = Caja.Pose()

    # 2. Movimiento interpolado
    for i in range(PASOS):
        frac = (i + 1) / PASOS
        dx = DESPLAZAMIENTO_MM * frac

        nueva_pose = pose_ini * robomath.transl(dx, 0, 0)
        Caja.setPose(nueva_pose)

        time.sleep(TIEMPO_TOTAL / PASOS)

    # 3. Borrar la caja
    Caja.Delete()





