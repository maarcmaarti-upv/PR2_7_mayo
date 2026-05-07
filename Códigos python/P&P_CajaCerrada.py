# RoboDK API
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
ACOLS = 4
FILAS = 3
DISTX = -310
DISTY = -260

TOTAL_POS = COLS * FILAS

FILE_INDEX = "paletizado_index.txt"

# Añade num de cajas a .txt
if os.path.exists(FILE_INDEX):
    with open(FILE_INDEX, "r") as f:
        index = int(f.read().strip())
else:
    index = 0

if index >= TOTAL_POS:
    index = 0

col = index % COLS
fila = index // COLS

# Movimientos
base_pre = target_Pre_Place.Pose()
base_place = target_PlaceCC.Pose()

desplazamiento = robomath.transl(col * DISTX, fila * DISTY, 0)

pose_pre = base_pre * desplazamiento
pose_place = base_place * desplazamiento

robot.MoveJ(target_Home1)
robot.setSpeed(100, 100)
robot.MoveJ(target_Pre_Pick)

robot.setSpeed(25, 20)
robot.MoveL(target_PickCC)

CajaCerrada.setParentStatic(RDK.ActiveStation())
VentosaPallet.AttachClosest('', 500)

robot.MoveL(target_Pre_Pick)

robot.setSpeed(100, 100)
robot.MoveJ(target_Home2)
robot.MoveJ(pose_pre)

robot.setSpeed(25, 20)
robot.MoveL(pose_place)

robot.setDO(1, 0)
VentosaPallet.DetachAll()

robot.MoveL(pose_pre)
robot.MoveJ(target_Home2)
robot.MoveJ(target_Home1)

with open(FILE_INDEX, "w") as f:
    f.write(str(index + 1))


