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


    

    while poging <= 5:

        print("Bekend woord:", bekend)

        gok = input("Raad het woord: ")


        

        if gok == woord:

            print("Goed geraden!")

            goed = True

            if team == 1:
                team1_score += 1
                team1_fout = 0

            else:
                team2_score += 1
                team2_fout = 0

            break


     

        for i in range(len(woord)):

            if gok[i] == woord[i]:

                print("GROEN", end=" ")

                bekend[i] = gok[i]

            elif gok[i] in woord:

                print("GEEL", end=" ")

            else:

                print("FOUT", end=" ")

        print()

        poging += 1


    

    if goed == False:

        print("Ronde verloren!")

        if team == 1:
            team1_fout += 1

        else:
            team2_fout += 1


    

    if goed == True:

        print("\nBallen trekken:")

        for i in range(2):

            bal = random.choice(ballenbak)

            print("Bal:", bal)


            

            if bal == "groen":

                if team == 1:
                    team1_groen += 1

                else:
                    team2_groen += 1


            

            elif bal == "rood":

                if team == 1:
                    team1_rood += 1

                else:
                    team2_rood += 1

                print("Rode bal! Geen tweede trek.")

                break


    # ================= FEATURE 11 - BALLEN TREKKEN =================

    if goed == True:

        print("\nBallen trekken:")

        for i in range(2):

            bal = random.choice(ballenbak)

            print("Bal:", bal)


            # ================= FEATURE 12 - GROENE BAL =================

            if bal == "groen":

                if team == 1:
                    team1_groen += 1

                else:
                    team2_groen += 1


            # ================= FEATURE 13 - RODE BAL =================

            elif bal == "rood":

                if team == 1:
                    team1_rood += 1

                else:
                    team2_rood += 1

                print("Rode bal! Geen tweede trek.")

                break


            # ================= FEATURE 14 - NUMMERBAL =================

            else:

                for rij in bingokaart:

                    for plek in range(len(rij)):

                        if rij[plek] == bal:
                            rij[plek] = "X"


    # ================= FEATURE 15 - BINGOKAART TONEN =================

    print("\nBINGOKAART")

    for rij in bingokaart:
        print(rij)


    # ================= FEATURE 16 - BINGO CONTROLEREN =================

    bingo = False


    # horizontaal

    for rij in bingokaart:

        if rij == ["X", "X", "X", "X"]:
            bingo = True


    # verticaal

    for i in range(4):

        if (
            bingokaart[0][i] == "X" and
            bingokaart[1][i] == "X" and
            bingokaart[2][i] == "X" and
            bingokaart[3][i] == "X"
        ):

            bingo = True


    # diagonaal

    if (
        bingokaart[0][0] == "X" and
        bingokaart[1][1] == "X" and
        bingokaart[2][2] == "X" and
        bingokaart[3][3] == "X"
    ):

        bingo = True


    