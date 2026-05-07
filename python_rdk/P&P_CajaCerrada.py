# RoboDK API

# En este código se usa Divide y Vencerás, que es la parte de PRA pedida para la entreda de PR2, para calcular las posiciones de las cajas.

from robodk import robolink, robomath
import os

RDK = robolink.Robolink()

robot = RDK.Item('ABBPallet', robolink.ITEM_TYPE_ROBOT)

# Targets
target_Home1 = RDK.Item('Home1', robolink.ITEM_TYPE_TARGET)
target_Home2 = RDK.Item('Home2', robolink.ITEM_TYPE_TARGET)
target_PickCC = RDK.Item('PickCC', robolink.ITEM_TYPE_TARGET)
target_Pre_Pick = RDK.Item('PrePickCC', robolink.ITEM_TYPE_TARGET)
target_Pre_Place = RDK.Item('PrePlaceCC', robolink.ITEM_TYPE_TARGET)
target_PlaceCC = RDK.Item('PlaceCC', robolink.ITEM_TYPE_TARGET)

CajaCerrada = RDK.Item('Caja_Movil_2', robolink.ITEM_TYPE_OBJECT)
VentosaPallet = RDK.Item('ventosa_pallet', robolink.ITEM_TYPE_TOOL)

robot.setPoseTool(VentosaPallet)

# Variables
COLS = 4
FILAS = 3
DISTX = -310
DISTY = -260

TOTAL_POS = COLS * FILAS

FILE_INDEX = "paletizado_index.txt"


# Algoritmo Divide y Vencerás para generar posiciones


def dividir_pallet(x0, y0, cols, filas, distx, disty):

    # Caso base:
    # Si solo queda una posicion, devolverla
    if cols == 1 and filas == 1:
        return [(x0, y0)]

    posiciones = []

    # Divide horizontalmente si hay varias columnas
    if cols > 1:

        mitad = cols // 2

        # Subproblema izquierda
        posiciones += dividir_pallet(
            x0,
            y0,
            mitad,
            filas,
            distx,
            disty
        )

        # Subproblema derecha
        posiciones += dividir_pallet(
            x0 + mitad * distx,
            y0,
            cols - mitad,
            filas,
            distx,
            disty
        )

    # Divide verticalmente si solo queda una columna
    elif filas > 1:

        mitad = filas // 2

        # Subproblema superior
        posiciones += dividir_pallet(
            x0,
            y0,
            cols,
            mitad,
            distx,
            disty
        )

        # Subproblema inferior
        posiciones += dividir_pallet(
            x0,
            y0 + mitad * disty,
            cols,
            filas - mitad,
            distx,
            disty
        )

    return posiciones

# Generar todas las posiciones del pallet

posiciones_pallet = dividir_pallet(
    0,
    0,
    COLS,
    FILAS,
    DISTX,
    DISTY
)

# Leer indice de caja desde archivo

if os.path.exists(FILE_INDEX):

    with open(FILE_INDEX, "r") as f:
        index = int(f.read().strip())

else:
    index = 0


# Reiniciar pallet cuando se llena

if index >= TOTAL_POS:
    index = 0


# Obtener posicion actual

x_desplazamiento, y_desplazamiento = posiciones_pallet[index]


# Calcular poses de colocacion

base_pre = target_Pre_Place.Pose()
base_place = target_PlaceCC.Pose()

desplazamiento = robomath.transl(
    x_desplazamiento,
    y_desplazamiento,
    0
)

pose_pre = base_pre * desplazamiento
pose_place = base_place * desplazamiento


# Movimientos robot

robot.MoveJ(target_Home1)

robot.setSpeed(100, 100)
robot.MoveJ(target_Pre_Pick)

robot.setSpeed(25, 20)
robot.MoveL(target_PickCC)


# Coger caja

CajaCerrada.setParentStatic(RDK.ActiveStation())

VentosaPallet.AttachClosest('', 500)

robot.MoveL(target_Pre_Pick)


# Ir a pallet

robot.setSpeed(100, 100)

robot.MoveJ(target_Home2)
robot.MoveJ(pose_pre)

robot.setSpeed(25, 20)

robot.MoveL(pose_place)


# Soltar caja

robot.setDO(1, 0)

VentosaPallet.DetachAll()


# Salida segura

robot.MoveL(pose_pre)

robot.MoveJ(target_Home2)
robot.MoveJ(target_Home1)


# Guardar siguiente posicion

with open(FILE_INDEX, "w") as f:
    f.write(str(index + 1))
