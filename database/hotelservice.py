from database.models import Hotel, Apartments
from database import get_db


def add_hotel_db(hotel_name: str,
                 hotel_location: str,
                 hotel_state: str,
                 hotel_city: str,
                 hotel_country: str,
                 hotel_contact: str,
                 hotel_star: int,
                 hotels_card_number: int):
    db = next(get_db())
    add_hotel = Hotel(hotel_name=hotel_name,
                      hotel_location=hotel_location,
                      hotel_state=hotel_state,
                      hotel_city=hotel_city,
                      hotel_country=hotel_country,
                      hotel_contact=hotel_contact,
                      hotel_star=hotel_star,
                      hotels_card_number=hotels_card_number)
    db.add(add_hotel)
    db.commit()
    return "Hotel Added"


def add_apartment_db(hotel_id: str,
                     apartments_number: int,
                     room_numbers: int,
                     room_amenity: str,
                     apartment_price: float,
                     status: bool):
    db = next(get_db())
    cheker_hotel_id = db.query(Hotel).filter_by(hotel_id=hotel_id).first()
    if cheker_hotel_id:
        add_apartment = Apartments(hotel_id=hotel_id,
                                   apartments_number=apartments_number,
                                   room_numbers=room_numbers,
                                   room_amenity=room_amenity,
                                   apartment_price=apartment_price,
                                   status=status)
        db.add(add_apartment)
        db.commit()

        return "Apartment Successfully Added"
    return "Wrong Hotel Id"


def delete_hotel_db(hotel_id: int):
    db = next(get_db())
    hotel = db.query(Hotel).filter_by(hotel_id=hotel_id).first()
    if hotel:
        db.delete(hotel)
        db.commit()
        return "Hotel Successfully Deleted"
    else:
        return "Hotel not Found"


def delete_apartment_db(apartments_number: int):
    db = next(get_db())
    apartment = db.query(Apartments).filter_by(apartments_number=apartments_number).first()
    if apartment:
        db.delete(apartment)
        db.commit()
        return "Apartment Deleted"
    else:
        return "Apartment not Found"


def get_hotels_db():
    db = next(get_db())
    hotels = db.query(Hotel).all()
    return hotels


def get_apartments_db(hotel_id: int):
    db = next(get_db())
    apartments = db.query(Apartments).filter_by(hotel_id=hotel_id).all()
    return apartments
