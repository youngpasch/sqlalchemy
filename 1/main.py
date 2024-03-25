from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_session.global_init("db/blogs.db")
    db_session.global_init("db/blogs.db")

    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = "21"
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(captain)
    db_sess.commit()

    colonist1 = User()
    colonist1.surname = "Scott"
    colonist1.name = "Ridley"
    colonist1.age = "21"
    colonist1.position = "captain"
    colonist1.speciality = "research engineer"
    colonist1.address = "module_1"
    colonist1.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(colonist1)
    db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()