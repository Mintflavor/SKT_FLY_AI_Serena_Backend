import warnings
from uuid import UUID

from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

warnings.simplefilter(action='ignore', category=FutureWarning)

letters_api = APIRouter(prefix='/letters', tags=['letters'])


class Letter(BaseModel):
    user_id: UUID
    title: str
    content: str


@letters_api.post("/")
async def create_diary():
    return HTTPException(status_code=501, detail="Not implemented")
