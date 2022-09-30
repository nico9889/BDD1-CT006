from __future__ import annotations

from typing import List
from random import choice, randint

N_PRODUTTORI = 50
N_PRODOTTI = 30  # PER PRODUTTORE


class Database:
    def __init__(self):
        pass

    def create(self):
        return "CREATE DATABASE gen172014;"


# Please forgive my ignorance in geography T_T
continents = {
    "Europa": ["ITA", "GER", "FRA"],
    "Asia": ["CHN", "JAP", "RUS"],
    "Oceania": ["AUS", "NZL", "PYF"],
    "America": ["USA", "MEX", "BRS"],
    "Africa": ["ZAF", "MAR", "EGY"]
}


def pick_letter() -> str:
    return str(chr(randint(ord("A") + 1, ord("z") - 1)))


class Produttore:
    _id: int = 1

    def __init__(self):
        self.id = Produttore._id
        Produttore._id += 1
        self.nome = pick_letter() + pick_letter() + pick_letter() + pick_letter() + pick_letter()
        self.continente = choice(list(continents.keys()))
        self.paese = choice(continents[self.continente])

    def insert(self):
        return f"INSERT INTO Produttori(IdProduttore, Nome, Paese, Continente) VALUES ({self.id}, '{self.nome}', '{self.paese}', '{self.continente}');"


class Produttori(List[Produttore]):
    def __init__(self):
        super().__init__()

    def create(self) -> str:
        return "CREATE TABLE IF NOT EXISTS Produttori(" \
               "IdProduttore INTEGER PRIMARY KEY NOT NULL," \
               "Nome VARCHAR(40) NOT NULL," \
               "Paese VARCHAR(3) NOT NULL UNIQUE," \
               "Continente VARCHAR(7) NOT NULL UNIQUE," \
               ");"


sets = ["Bicchieri", "Posate", "Piatti", "Punte", "Cacciaviti", "Pentole", "Carte Pokémon", "Chiavi inglesi",
        "Coltelli", "Forbici", "Pennarelli", "Pastelli", "Attrezzi", "Brugole", "Tovaglioli"]
aggettivi = ["Elegante", "Carino", "Raro", "Alla moda", "Unico", "Nuovo", "Usato", "Fragile", "Scadente", "Storico",
             "Minimale"]


class Prodotto:
    _id: int = 1

    def __init__(self, id_produttore: int):
        self.id = Prodotto._id
        Prodotto._id += 1
        self.nome = f"Set di {choice(sets)} {choice(aggettivi)}"
        self.prezzo = randint(100, 1000) / 100
        self.id_produttore = id_produttore

    def insert(self):
        return f"INSERT INTO Prodotti(IdProdotto, Nome, Prezzo, IdProduttore) VALUES ({self.id}, '{self.nome}', {self.prezzo}, {self.id_produttore});"


class Prodotti(List[Prodotto]):
    def __init__(self):
        super().__init__()

    def create(self):
        return "CREATE TABLE IF NOT EXISTS Prodotti(" \
               "IdProdotto INTEGER PRIMARY KEY NOT NULL," \
               "Nome VARCHAR(40) NOT NULL," \
               "Prezzo FLOAT NOT NULL," \
               "IdProduttore INTEGER NOT NULL," \
               "FOREIGN KEY(IdProduttore) REFERENCES Produttori(IdProduttore)" \
               ");"


if __name__ == "__main__":
    db = Database()
    produttori = Produttori()
    prodotti = Prodotti()
    for _ in range(0, N_PRODOTTI):
        produttore = Produttore()
        produttori.append(produttore)
        for _ in range(0, N_PRODOTTI):
            prodotti.append(Prodotto(produttore.id))
    print(db.create())
    print(produttori.create())
    print(prodotti.create())

    for produttore in produttori:
        print(produttore.insert(), "\n")
    for prodotto in prodotti:
        print(prodotto.insert(), "\n")
