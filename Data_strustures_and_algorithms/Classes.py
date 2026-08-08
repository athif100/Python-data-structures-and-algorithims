#A class is used to represent an object with multiple attributes
class Vehical:
  Brand=""
  Color=""
  Maxsp=100
Tesla=Vehical()
Tesla.Brand="Tesla"
Tesla.Color="Black"
Tesla.Maxsp=190
print(Tesla.Maxsp)
Mclerane=Vehical()
Mclerane.Brand="Mclerane"
Mclerane.Color="Silver"
Mclerane.Maxsp=350
Vehical.Maxsp=67
print(Mclerane.Maxsp)
print(Tesla.Maxsp)
class Vehical2:
  def __init__(self,Brand,Color,Maxsp):
    self.Brand=Brand
    self.Color=Color
    self.Maxsp=Maxsp
Porche=Vehical2("Porche","Red",150)
print(Porche.Color)
