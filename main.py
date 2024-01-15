from infrastructure.Repo import Repo

def main():
    repo = Repo()
    repo.addF(1,"Ana","italian",3)
    repo.addF(2,"Carla","american",4)
    repo.addF(3,"Mihai","italian",5)
    while(True):
        try:
            print("0.Exit\n1.Add\n2.Remove\n3.Get\n4.Print\n")
            print(repo)
            cmd = int(input("choose"))
            if cmd == 0:
                break
            elif cmd ==1 :
                id = int(input("id"))
                name = input("name")
                tema = input("tema")
                rating = int(input("raiting"))
                repo.addF(id, name,tema,rating)
            elif cmd ==2:
                raiting = int(input("raiting"))
                repo.removeF(raiting)
            elif cmd ==3:
                tema = input("tema")
                print(repo.getF(tema))
            elif cmd ==4:
                print(repo)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print (e)

main()