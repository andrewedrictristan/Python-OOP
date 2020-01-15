from Raum import Raum

class Büro(Raum):

    def __init__(self,Fläche):
        super().__init__(Fläche)
        self.name_list = []

    def __str__(self):
        return 'Fläche: {self.Fläche} m² Namesliste: {self.name_list}'.format(self=self)

    def AddName(self,name):
        self.name_list.append(name)

    def SubName(self,name):
        self.name_list.remove(name)

    def CalcMiete(self):
        return 100.0


# büro1 = Büro(30)
# büro2 = Büro(40)
#
# büro1.AddName ('Roger Rabbit')
# büro1.AddName ('Yosemite Sam Elmer Fudd')
# büro2.AddName (' pinky brain')
# büro2.AddName ('Wile Coyote')
# büro2.AddName ('Speedy Gonzales')
# print (büro1)
# print (büro2)
# büro2.SubName ('Wile Coyote')
# print (büro2)
# print (f'Miete Büro 1: {büro1.CalcMiete()}')