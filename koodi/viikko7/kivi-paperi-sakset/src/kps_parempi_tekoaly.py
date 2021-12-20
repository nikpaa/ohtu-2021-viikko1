from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly:
     def pelaa(self):
        tuomari = Tuomari()
        tekoaly = TekoalyParannettu(10)

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self.is_move_ok(ekan_siirto) and self.is_move_ok(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")
            tekoaly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

     def is_move_ok(self, siirto):
         return siirto == "k" or siirto == "p" or siirto == "s"