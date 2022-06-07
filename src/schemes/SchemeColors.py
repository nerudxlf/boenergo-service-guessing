import pydantic


class SchemeColorAnswer(pydantic.BaseModel):
    result: bool
    service: str
    user: str

