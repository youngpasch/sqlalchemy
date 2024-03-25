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
    colonist1.surname = "A"
    colonist1.name = "A"
    colonist1.age = "1"
    colonist1.position = "colonist"
    colonist1.speciality = "pilot"
    colonist1.address = "module_1"
    colonist1.email = "AAAAAA@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(colonist1)
    db_sess.commit()

    colonist2 = User()
    colonist2.surname = "B"
    colonist2.name = "B"
    colonist2.age = "2"
    colonist2.position = "colonist"
    colonist2.speciality = "doctor"
    colonist2.address = "module_1"
    colonist2.email = "BBBBBBB@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(colonist2)
    db_sess.commit()

    colonist3 = User()
    colonist3.surname = "C"
    colonist3.name = "C"
    colonist3.age = "3"
    colonist3.position = "colonist"
    colonist3.speciality = "scientist"
    colonist3.address = "module_1"
    colonist3.email = "CCCCCC@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(colonist3)
    db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()