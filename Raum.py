class Raum:

    def __init__(self, Fläche):
        self.Fläche = Fläche

    def __str__(self):
        return 'Fläche: {self.Fläche} m²'.format(self=self)


    def GetFläche(self):
        return self.Fläche

    def CalcMiete(self):
        return self.Fläche * 10



# raum1 = Raum(15)
# raum2 = Raum (100)
# print(raum1)
# print(raum2)
# print(f'Raum 1: {raum1.GetFläche()}, Miete: {raum1.CalcMiete()} €')
# print(f'Raum 2: {raum2.GetFläche()}, Miete: {raum2.CalcMiete()} €')


