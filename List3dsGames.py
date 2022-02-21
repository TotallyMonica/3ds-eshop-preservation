import csv

# import 3DS.csv as games
def importGames (gameCSV):
    print("Games CSV was successfully imported.")

def listGames (gameCSV):
    print("The imported games are as listed here: ")
    for entry in gameCSV:
        print(entry["Title"])

if __name__ == "__main__":
    games = open('3DS.csv','r')
    importGames(games)
    listGames(games)
    games.close()