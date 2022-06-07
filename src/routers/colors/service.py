from sqlalchemy import orm
import random

from src.database.db_model import Colors, ColorNames
from src.schemes.SchemeColors import SchemeColorAnswer


async def service_colors(id: int, db: orm.Session) -> SchemeColorAnswer:
    """
    Compare results
    :param id:
    :param db:
    :return: SchemeColorAnswer
    """
    user_color = db.query(Colors).filter(Colors.id == id).first()
    system_color = db.query(ColorNames).all()
    system_color_get = random.choice(system_color)
    if user_color.color_name.name == system_color_get.name:
        answer = True
        service = system_color_get.name
        user = user_color.color_name.name
    else:
        answer = False
        service = system_color_get.name
        user = user_color.color_name.name
    return SchemeColorAnswer(result=answer, service=service, user=user)
