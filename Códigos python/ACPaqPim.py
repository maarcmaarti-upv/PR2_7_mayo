from robodk import robolink
from robodk import robomath

RDK = robolink.Robolink()

# Declaraciones
Cinta = RDK.Item('CRPaq')
SistRefCinta = RDK.Item('BasePaq')
INCREMENTO_MM = 880

# Movimiento
if Cinta.Valid():

    joints = Cinta.Joints().list()
    joints[0] += INCREMENTO_MM
    Cinta.MoveJ(joints)
