import os
os.system("cls")
from models.user import User
from dao.factory import get_dao_from_config
import pyodbc

def main():
    dao = get_dao_from_config("config.json")

    dao.add_user(User(None, "lolsssa ", "asljuslsffs@example.com"))
    dao.add_user(User(None, "Marsiall", "desasetllttre@gmail.com"))

    print("Usuarios almacenados:")
    for u in dao.get_all_users():
        print(u)

if __name__ == "__main__":
    main()
