from robodk import robolink

# Este programa resetea los paqutes a la posición inicial

RDK = robolink.Robolink()


cintas = ['CRPaq']

for nombre in cintas:
    cinta = RDK.Item(nombre)
    if cinta.Valid():
        cinta.setJoints([0])
