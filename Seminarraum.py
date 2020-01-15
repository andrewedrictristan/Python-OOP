from Raum import Raum


class Seminarraum(Raum):

    def __init__(self,Fläche, Plätze):
        super().__init__(Fläche)
        self.Plätze = Plätze


    def __str__(self):
        return 'Fläche: {self.Fläche} m² Plätze: {self.Plätze}'.format(self=self)

    def SetPlätze(self, Plätze):
        self.Plätze = Plätze

    def GetPlätze (self):
        return self.Plätze

    def CalcMiete(self):
        return self.Fläche * 8

#
# seminar1 = Seminarraum (100, 40)
# print (seminar1)
# seminar2 = Seminarraum (200, 70)
# print (seminar2)
#
# seminar1.SetPlätze (50)
# print (f'Plätze 1: {seminar1.GetPlätze()}, Miete: {seminar1.CalcMiete()} €')
# print (f'Plätze 2: {seminar2.GetPlätze()}, Miete: {seminar2.CalcMiete()} €')