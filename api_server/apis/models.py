import warnings
from enum import Enum

from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from . import MeloDB, str_to_object_id, object_id_to_str

warnings.simplefilter(action='ignore', category=FutureWarning)

MeloDB = MeloDB()
models_api = APIRouter(prefix='/models', tags=['models'])


# class ContentType(str, Enum):
#     diary = 'diary'
#     letter = 'letter'
#     chat = 'chat'


class Genre(str, Enum):
    classic = 'classic'
    jazz = 'jazz'
    pop = 'pop'
    rock = 'rock'
    hiphop = 'hiphop'


class Instrument(str, Enum):
    piano = 'piano'
    guitar = 'guitar'
    drum = 'drum'
    organ = 'organ'
    clarinet = 'clarinet'


class Speed(str, Enum):
    slow = 'slow'
    medium = 'medium'
    fast = 'fast'


class Duration(str, Enum):
    ten_seconds = '10s'
    thirty_seconds = '30s'
    one_minute = '1m'
    one_minute_thirty_seconds = '1m30s'
    two_minutes = '2m'


class ImageGenerateQuery(BaseModel):
    user_id: str
    baby_id: str
    # content_type: ContentType
    # content_id: str
    genre: Genre
    instrument: Instrument
    speed: Speed
    duration: Duration


class MusicGenerateQuery(BaseModel):
    user_id: str
    baby_id: str
    # content_type: ContentType
    # content_id: str
    genre: Genre
    instrument: Instrument
    speed: Speed
    duration: Duration


# 생성 앨범아트 이미지 생성하기
@models_api.post("/images")
async def create_generated_albumart_image(item: ImageGenerateQuery):
    # content_type_map = {
    #     ContentType.diary: MeloDB.melo_diaries,
    #     ContentType.letter: MeloDB.melo_letters,
    #     ContentType.chat: MeloDB.melo_chats,
    # }
    #
    # content_id = str_to_object_id(item.content_id)
    # content = content_type_map[item.content_type].find_one({"_id": content_id, "user_id": item.user_id, "baby_id": item.baby_id})
    # if not content:
    #     raise HTTPException(status_code=404, detail="Not found")

    # -------------------------------------------
    # # TODO: 모델에 이미지 생성 요청하는 코드 작성
    # -------------------------------------------

    # image_id = MeloDB.melo_images.insert_one(item.model_dump(mode='json')).inserted_id
    #
    # return JSONResponse(status_code=201, content={"image_id": str(image_id)})

    raise HTTPException(status_code=501, detail="Not implemented (create_generated_albumart_image)")


# 생성 앨범아트 이미지 가져오기
@models_api.get("/images")
async def get_generated_albumart_image(user_id: str, baby_id: str, image_id: str):
    image_id = str_to_object_id(image_id)
    image = MeloDB.melo_images.find_one({"_id": image_id, "user_id": user_id, "baby_id": baby_id})
    if not image:
        raise HTTPException(status_code=404, detail="Not found")

    image['_id'] = str(image['_id'])

    return JSONResponse(status_code=200, content=image['content'])


# 생성 앨범아트 이미지 제거
@models_api.delete("/images")
async def delete_generated_albumart_image(user_id: str, baby_id: str, image_id: str):
    image_id = str_to_object_id(image_id)
    image = MeloDB.melo_images.find_one({"_id": image_id, "user_id": user_id, "baby_id": baby_id})
    if not image:
        raise HTTPException(status_code=404, detail="Not found")

    MeloDB.melo_images.delete_one({"_id": image_id, "user_id": user_id, "baby_id": baby_id})

    return JSONResponse(status_code=200, content={"image_id": str(image_id)})


# 생성 음악 생성하기
@models_api.post("/music")
async def create_generated_music(item: MusicGenerateQuery):
    # content_type_map = {
    #     ContentType.diary: MeloDB.melo_diaries,
    #     ContentType.letter: MeloDB.melo_letters,
    #     ContentType.chat: MeloDB.melo_chats,
    # }
    #
    # content_id = str_to_object_id(item.content_id)
    # content = content_type_map[item.content_type].find_one({"_id": content_id, "user_id": item.user_id, "baby_id": item.baby_id})
    # if not content:
    #     raise HTTPException(status_code=404, detail="Not found")

    user = MeloDB.melo_users.find_one({"_id": str_to_object_id(item.user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User Not found")

    baby = MeloDB.melo_babies.find_one({"_id": str_to_object_id(item.baby_id)})
    if not baby:
        raise HTTPException(status_code=404, detail="Baby Not found")

    # -------------------------------------------
    # # TODO: 모델에 음악 생성 요청하는 코드 작성
    # -------------------------------------------

    item = item.model_dump(mode='json')
    item['music_url'] = None

    music_id = MeloDB.melo_music.insert_one(item).inserted_id

    return JSONResponse(status_code=202, content={"music_id": str(music_id)})

    # raise HTTPException(status_code=501, detail="Not implemented (create_generated_music)")


# 생성 음악 가져오기
@models_api.get("/music")
async def get_generated_music(user_id: str, baby_id: str, music_id: str):
    music_id = str_to_object_id(music_id)
    music = MeloDB.melo_music.find_one({"_id": music_id, "user_id": user_id, "baby_id": baby_id})
    if not music:
        raise HTTPException(status_code=404, detail="Not found")

    music['id'] = str(music['_id'])

    return JSONResponse(status_code=200, content=music)


# 생성 음악 제거
@models_api.delete("/music")
async def delete_generated_music(user_id: str, baby_id: str, music_id: str):
    music_id = str_to_object_id(music_id)
    music = MeloDB.melo_music.find_one({"_id": music_id, "user_id": user_id, "baby_id": baby_id})
    if not music:
        raise HTTPException(status_code=404, detail="Not found")

    MeloDB.melo_music.delete_one({"_id": music_id, "user_id": user_id, "baby_id": baby_id})

    return JSONResponse(status_code=200, content={"music_id": str(music_id)})