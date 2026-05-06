from robodk import robolink
from robodk import robomath

RDK = robolink.Robolink()

Cinta = RDK.Item('CRPaq')
SistRefCinta = RDK.Item('BasePaq')
INCREMENTO_MM = 880

if Cinta.Valid():

    joints = Cinta.Joints().list()
    joints[0] += INCREMENTO_MM
    Cinta.MoveJ(joints)
