def Eintragen( Zahl):
        X = open('Datenbank-Highscore.txt', 'a')
        X.write(Zahl)
        X.write('\n')
        X.close()
def Ausgeben():
        X = open('Datenbank-Highscore.txt').read()
        print(X)
def Sortieren():
        Liste = []
        b = -1
        X = open('Datenbank-highscore.txt').readlines()
        Laenge = len(X) -1 
        while True:
            X = open('Datenbank-highscore.txt').readlines()
            b = b + 1
            Liste.append(X[b])
            if b == Laenge:
                break
        if Laenge >= 2:
            Liste.sort()
            Liste.reverse()
            X = open('Datenbank-Highscore.txt', 'w')
            X.write(Liste[0])
            X.close
            X = open('Datenbank-Highscore.txt', 'a')
            b = 0
            while True:
                b = b + 1
                X.write(Liste[b])
                if b == Laenge:
                    break
            X.close()
