from robodk import robolink

RDK = robolink.Robolink()


cintas = ['CRPaq']

for nombre in cintas:
    cinta = RDK.Item(nombre)
    if cinta.Valid():
        cinta.setJoints([0])
