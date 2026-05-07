import time
from robodk import robolink
from robodk import robomath

RDK = robolink.Robolink()

CajaBase = RDK.Item('CajaCerrada')
SistRefCinta = RDK.Item('CCBase')

# Variables
DESPLAZAMIENTO_MM = 910
TIEMPO_TOTAL = 1.5
PASOS = 60

if CajaBase.Valid() and SistRefCinta.Valid():

    # Crear copia
    CajaBase.Copy()
    Caja = RDK.Paste(SistRefCinta)
    Caja.setName('Caja_Movil_2')

    pose_ini = Caja.Pose()

    # Movimiento interpolado
    for i in range(PASOS):
        frac = (i + 1) / PASOS
        dx = DESPLAZAMIENTO_MM * frac

        pose = pose_ini * robomath.transl(dx, 0, 0)
        Caja.setPose(pose)

        time.sleep(TIEMPO_TOTAL / PASOS)

   
