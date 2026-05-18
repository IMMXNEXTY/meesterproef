from woordenlijst import kies_woord
import random


team = 1

team1_score = 0
team2_score = 0

team1_rood = 0
team2_rood = 0

team1_groen = 0
team2_groen = 0

team1_fout = 0
team2_fout = 0


ballenbak = [
    "groen", "groen", "groen",
    "rood", "rood", "rood",
    2, 4, 6, 8,
    1, 3, 5, 7
]


bingokaart = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]



while True:

    print("\n================")
    print("LINGO")
    print("================")

    print("Team", team, "is aan de beurt")


    woord = random.choice(kies_woord)

    print("Beginletter:", woord[0])

    poging = 1
    goed = False

    bekend = [woord[0]]

    for i in range(len(woord) - 1):
        bekend.append("_")


    