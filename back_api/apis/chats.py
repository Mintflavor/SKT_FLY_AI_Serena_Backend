import warnings

from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

warnings.simplefilter(action='ignore', category=FutureWarning)

chats_api = APIRouter(prefix='/chats', tags=['chats'])


class Chat(BaseModel):
    user_id: str
    title: str
    content: str


# {
#     "user_id": "550e8400-e29b-41d4-a716-446655440000",
#     "title": "제목",
#     "content": "내용"
# }


# 채팅 작성
@chats_api.post("/")
async def create_chat(item: Chat):
    raise HTTPException(status_code=501, detail="Not implemented (create_chat)")


# 전체 채팅 조회
@chats_api.get("/{user_id}")
async def get_chats(user_id: str):
    raise HTTPException(status_code=501, detail="Not implemented (get_chats)")


# 특정 채팅 조회
@chats_api.get("/{user_id}/{chat_id}")
async def get_chat(user_id: str, chat_id: str):
    raise HTTPException(status_code=501, detail="Not implemented (get_chat)")


# 채팅 삭제
@chats_api.delete("/{user_id}/{chat_id}")
async def delete_chat(user_id: str, chat_id: str):
    raise HTTPException(status_code=501, detail="Not implemented (delete_chat)")
