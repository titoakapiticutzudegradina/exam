from infrastructure.Repo import Repo

def main():
    repo = Repo()
    repo.addC("Mihai",4.0,12.0,11.0,True)
    repo.addC("Alex",1.0,1.0,1.0,False)
    repo.addC("Claudiu",3.0,7.0,1.0,False)
    while(True):
        try:
            print("0.Exit\n1.Add\n2.sort\n3.remove\n4.print")
            print(repo)
            cmd = int(input("choose"))
            if cmd == 0:
                break
            elif cmd==1:
                name = input("detinator")
                latime = float(input("latime"))
                inaltime = float(input("inaltime"))
                lungime = float(input("lungime"))
                fert = bool(input("fertilitate"))
                repo.addC(name,latime,inaltime,lungime,fert)
            elif cmd==2:
                repo.sortC()
                print(repo)
            elif cmd==3:
                repo.removeC()
            elif cmd == 4:
                print(repo)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

main()