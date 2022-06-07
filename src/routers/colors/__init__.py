from fastapi import APIRouter, Depends, Body
from sqlalchemy import orm

from src.database.db_connect import get_db
from src.routers.colors.controller import controller_colors
from src.schemes.SchemeColors import SchemeColorAnswer

router = APIRouter(
    prefix="/api/colors",
    tags=["colors"],
    responses={404: {"description": "Not found"}}
)


@router.post('/', response_model=SchemeColorAnswer)
async def colors(id: int = Body(embed=True), db: orm.Session = Depends(get_db)):
    """
    Route for guessing color
    :param id: Color number selected by the user
    :param db: Current db Session
    :return:
    """
    result = await controller_colors(id, db)
    return result
