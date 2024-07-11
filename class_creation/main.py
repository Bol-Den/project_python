
from Car import Cars

bmw = Cars("red", "petrol")

bmw_color = bmw.getColor()
bmw_engine = bmw.getEngine()

print(bmw_color)
print(bmw_engine)

bmw.setNewColor("black")
bmw_color = bmw.getColor()
print(bmw_color)
