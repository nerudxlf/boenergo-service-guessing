import random

from src.database.db_connect import get_db
from src.database.db_model import ColorNames, Colors


def insert_color_names():
    db, *_ = get_db()
    blue = ColorNames(
        name="blue"
    )
    green = ColorNames(
        name="green"
    )
    red = ColorNames(
        name="red"
    )
    db.add(blue)
    db.add(green)
    db.add(red)
    db.commit()


def insert_data():
    db, *_ = get_db()
    for i in range(0, 100):
        rand = int(random.random() * 100)
        if rand <= 70:
            color = Colors(name_id=1)
        elif 70 < rand <= 87:
            color = Colors(name_id=2)
        else:
            color = Colors(name_id=3)
        db.add(color)
    db.commit()

