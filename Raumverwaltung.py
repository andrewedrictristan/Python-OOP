from Seminarraum import Seminarraum
from Büro import Büro


class Raumverwaltung:

    def __init__(self):
        self.FB1RaumTabelle = {}
        self.FB2RaumTabelle = {}
        self.Raumnummer = 100

    def AddRaum(self, FB, Raum):
        if FB == 1:
            nummer = self.Raumnummer
            self.FB1RaumTabelle[nummer] = Raum
            self.Raumnummer += 1
            return nummer
        elif FB == 2:
            nummer = self.Raumnummer
            self.FB2RaumTabelle[nummer] = Raum
            self.Raumnummer += 1
            return nummer

        else:
            return -1

    def PrintRäume(self):
        for key, value in self.FB1RaumTabelle.items():
            print("FB1 ", key, value)
        for key, value in self.FB2RaumTabelle.items():
            print("FB2 ", key, value)

    def Umwidmung(self, Raumnummer):
        if Raumnummer in self.FB1RaumTabelle:
            self.FB2RaumTabelle[Raumnummer] = self.FB1RaumTabelle[Raumnummer]
            del self.FB1RaumTabelle[Raumnummer]
        elif Raumnummer in self.FB2RaumTabelle:
            self.FB1RaumTabelleRaumTabelle[Raumnummer] = self.FB2RaumTabelle[Raumnummer]
            del self.FB2RaumTabelle[Raumnummer]

    def CalcMiete(self, FB):

        if FB == 1:
            calc__1 = 0
            for i in range(100,110):
                a = self.FB1RaumTabelle.get(i)
                if a == büro1:
                    calc1 = büro1.CalcMiete()
                    calc__1 = calc__1 + calc1

                elif a == büro2:
                    calc2 = büro2.CalcMiete()
                    calc__1 = calc__1 + calc2

                elif a == seminar1:
                    calc3= seminar1.CalcMiete()
                    calc__1 = calc__1 + calc3

                elif a == seminar2:
                    calc4= seminar2.CalcMiete()
                    calc__1 = calc__1 + calc4

            return calc__1

        if FB == 2:
            calc__2 = 0
            for i in range(100, 110):
                a = self.FB2RaumTabelle.get(i)
                if a == büro1:
                    calc1 = büro1.CalcMiete()
                    calc__2 = calc__2 + calc1


                elif a == büro2:
                    calc2 = büro2.CalcMiete()
                    calc__2 = calc__2 + calc2


                elif a == seminar1:
                    calc3 = seminar1.CalcMiete()
                    calc__2 = calc__2 + calc3


                elif a == seminar2:
                    calc4 = seminar2.CalcMiete()
                    calc__2 = calc__2 + calc4


            return calc__2


seminar1 = Seminarraum(100, 40)
seminar2 = Seminarraum(200, 70)
büro1 = Büro(30)
büro2 = Büro(40)

büro1.AddName('Elmer Fudd')
büro2.AddName('Wile Coyote')
büro2.AddName('Speedy Gonzales')

manager = Raumverwaltung()
s1 = manager.AddRaum(1, seminar1)
s2 = manager.AddRaum(2, seminar2)
b1 = manager.AddRaum(1, büro1)
b2 = manager.AddRaum(1, büro2)
manager.PrintRäume()
manager.Umwidmung(b2)
manager.PrintRäume()

print(f'Miete FB1: {manager.CalcMiete(1)} €')
print(f'Miete FB2: {manager.CalcMiete(2)} €')
