import numpy as np


class ZasadyGry:
    # KONSTRUKTOR
    def __init__(self, zasady_zycia, zasady_ozywania):
        # TABELE WYPEŁNIONE 0
        self.zasady_zycia = np.zeros(10, dtype=int)
        self.zasady_ozywania = np.zeros(10, dtype=int)

        # Ustalenie, ile sąsiadów musi mieć komórka, aby przeżyć (pozostałe opcje umrą)
        for c in zasady_zycia:
            i = int(c)
            # 8 - bo chcemy rozpatrzeć wszystkie scenariusze
            # — biorąc pod uwagę sąsiedztwo Moore'a (ile komórek jest dookoła rozpatrywanej komórki)
            if i <= 8:
                self.zasady_zycia[i] = 1

        # Ustalenie, ile sąsiadów musi mieć komórka, aby ożyć
        for c in zasady_ozywania:
            j = int(c)
            # 8 - bo chcemy rozpatrzeć wszystkie scenariusze
            # — biorąc pod uwagę sąsiedztwo Moore'a (ile komórek jest dookoła rozpatrywanej komórki)
            if j <= 8:
                self.zasady_ozywania[j] = 1

    # Metoda sprawdza, czy komórka ma na tyle sąsiadów, żeby żyć
    def powinna_zyc(self, wartosc_sasiada):
        # 1 - jak tak
        # 0 - jak nie
        return 1 if self.zasady_zycia[wartosc_sasiada] > 0 else 0

    # Metoda sprawdza, czy komórka ma na tyle sąsiadów, żeby ożyć
    def powinna_ozyc(self, wartosc_sasiada):
        # 1 - jak tak
        # 0 - jak nie
        return 1 if self.zasady_ozywania[wartosc_sasiada] > 0 else 0


class GameOfLife:

    # KONSTRUKTOR
    def __init__(self, rozmiar_siatki, zasady_zycia):
        self.rozmiar = rozmiar_siatki
        self.zasady_zycia = zasady_zycia
        # TABELE WYPEŁNIONE 0
        self.pole = np.zeros((rozmiar_siatki, rozmiar_siatki), dtype=int)
        self.nowe_pole = np.zeros((rozmiar_siatki, rozmiar_siatki), dtype=int)

    def inicjalzacja_pola(self, x, y):
        # Ustawienie komórki na planszy
        self.pole[x][y] = 1

    # Wypisywanie całego pola
    def wypisz_pola(self):
        for i in range(self.rozmiar):
            for j in range(self.rozmiar):
                print('■' if self.pole[i][j] == 1 else '0', end=' ')
            print()

    def iteruj(self):
        for x in range(self.rozmiar):
            for y in range(self.rozmiar):

                # Meshgrid pozwala na utworzenie siatki zawierającej wszystkie możliwe kombinacje współrzędnych
                aktualny_x, aktualny_y = np.meshgrid(
                    # Siatka jest cykliczna, czyli komórki na krawędzi mają sąsiadów po przeciwnej stronie siatki
                    np.mod(np.arange(x - 1, x + 2), self.rozmiar),
                    np.mod(np.arange(y - 1, y + 2), self.rozmiar),
                    # Kształt wynikowej siatki to len(x) na len(y)
                    indexing="ij",
                )
                # Obliczamy sumę wartości sąsiadów. Odejmujemy wartość samej komórki (interesują nas tylko sąsiedzi)
                wartosci_sasiadow = np.sum(self.pole[aktualny_x, aktualny_y]) - self.pole[x, y]

                if self.pole[x][y] == 1:
                    self.nowe_pole[x][y] = self.zasady_zycia.powinna_zyc(wartosci_sasiadow)
                else:
                    self.nowe_pole[x][y] = self.zasady_zycia.powinna_ozyc(wartosci_sasiadow)

        # Aktualizujemy pole do nowego stanu
        self.pole = np.copy(self.nowe_pole)


def main():
    rozmiar_siatki = int(input("Rozmiar siatki: "))
    zasady_zycia = input("Zasady dla życia: ")
    zasady_ozywiania = input("Zasady dla ożywiania: ")
    zasady_gry = ZasadyGry(zasady_zycia, zasady_ozywiania)
    gra = GameOfLife(rozmiar_siatki, zasady_gry)

    # TZW Glider
    gra.inicjalzacja_pola(15, 15)
    gra.inicjalzacja_pola(16, 15)
    gra.inicjalzacja_pola(17, 15)
    gra.inicjalzacja_pola(17, 14)
    gra.inicjalzacja_pola(16, 13)

    input("Pierwsza iteracja")
    maksymalny_rozmiar = rozmiar_siatki - 1
    print(gra.pole[maksymalny_rozmiar][maksymalny_rozmiar])

    while True:
        input_uzytkownika = input()
        if input_uzytkownika == "q":
            break

        gra.wypisz_pola()
        gra.iteruj()


if __name__ == "__main__":
    main()  # 20,23,3
