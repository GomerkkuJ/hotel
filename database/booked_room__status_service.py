from database.models import BookingForm
from database import get_db
from datetime import date


def add_booked_room_db(apartment_id: int,
                       check_in: date,
                       check_out: date,
                       user_id: int):
    db = next(get_db())

    book_room = BookingForm(apartment_id=apartment_id,
                            check_in=check_in,
                            check_out=check_out,
                            user_id=user_id)
    db.add(book_room)
    db.commit()
    return True


def delete_booked_room_db(booking_id: int):
    db = next(get_db())
    room = db.query(BookingForm).filter_by(booking_id=booking_id).first()
    if room:
        db.delete(room)
        db.commit()
        return False
    else:
        return True


def get_books_by_user_id(user_id: int):
    db = next(get_db())
    books = db.query(BookingForm).filter_by(user_id=user_id).all()
    return books
