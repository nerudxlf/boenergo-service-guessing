from fastapi import HTTPException, status
from sqlalchemy import orm

from src.routers.colors.service import service_colors
from src.schemes.SchemeColors import SchemeColorAnswer


async def controller_colors(id: int, db: orm.Session) -> SchemeColorAnswer:
    """
    Checking for Errors and getting answer
    :param id:
    :param db:
    :return: SchemeColorAnswer
    """
    if not (0 < id <= 100):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Value Error")
    result = await service_colors(id, db)
    return result
