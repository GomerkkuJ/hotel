from booked_rooms.payment import payment_international
from database.booked_room__status_service import add_booked_room_db, delete_booked_room_db, get_books_by_user_id
from datetime import datetime, date
from fastapi import APIRouter

book = APIRouter(prefix="/hotel/api", tags=["Book Service"])


@book.post('/add_booked_room')
async def add_booked_room_api(
        apartment_id: int, check_in: date,
        check_out: date, user_id: int, card_date: str, csv: int,
        card_number: int,
):
    if len(str(csv)) < 3 or len(str(card_number)) < 16:
        return {"message": "Wrong card data"}
    payment_international(card_number=card_number, card_date=card_date, csv=csv)
    result = add_booked_room_db(apartment_id=apartment_id,
                                check_in=check_in,
                                check_out=check_out,
                                user_id=user_id)
    return {"status": 1, "message": result}


@book.delete('/delete_booked_room')
async def delete_booked_room_api(booking_id: int):
    result = delete_booked_room_db(booking_id=booking_id)
    return {"status": 1, "message": result}


@book.get("/get_book_room")
async def get_books(user_id: int):
    result = get_books_by_user_id(user_id=user_id)
    return result
