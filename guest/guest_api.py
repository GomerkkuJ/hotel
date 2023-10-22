from fastapi import APIRouter

from database.guestservice import register_user_db, check_password_db, delete_user_db, get_user_cabinet_db, \
    get_user_card_db


guest = APIRouter(prefix="/hotel/api", tags=["UserService"])


@guest.post('/register_guests')
async def register_user_api(user_phone_number: int, user_name: str, password: str, user_email: str):
    result = register_user_db(user_phone_number=user_phone_number, user_name=user_name, password=password,
                              user_email=user_email)
    if isinstance(result, str):
        return result
    else:
        return {'status': 1, "message": result.get("message"), "user_id": result.get("user_id")}


@guest.post('/login')
async def login_user_api(user_email: str, password: str):
    result = check_password_db(user_email=user_email, password=password)
    return {'status': 1, "message": result}


@guest.delete('/delete-user')
async def delete_user_api(user_id: int):
    result = delete_user_db(user_id=user_id)
    return {"status": 1, "message": result}


# вывод личных данных
@guest.get('/user_cabinet')
async def get_user_cabinet_api(user_id: int):
    result1 = get_user_cabinet_db(user_id=user_id)
    result2 = get_user_card_db(user_id=user_id)
    if isinstance(result1, str) and isinstance(result2, str):
        return {'status': 0, "message": result1 + result2}
    elif not isinstance(result1, str) and isinstance(result2, str):
        return {"status": 1, "user": result1}
    else:
        return {"status": 1, "user": result1, "card": result2}
