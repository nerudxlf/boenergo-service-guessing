from fastapi import FastAPI

from src.routers import colors

app = FastAPI()

app.include_router(colors.router)