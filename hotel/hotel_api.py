from fastapi import APIRouter

from database import add_apartment_db, add_hotel_db, delete_hotel_db, delete_apartment_db, get_hotels_db, \
    get_apartments_db

hotel = APIRouter(prefix="/hotel/api", tags=["Hotel Service"])


@hotel.post('/add_hotel')
async def add_hotel_api(hotel_name: str,
                        hotel_location: str,
                        hotel_state: str,
                        hotel_city: str,
                        hotel_country: str,
                        hotel_contact: str,
                        hotel_star: int,
                        hotels_card_number: int):
    result = add_hotel_db(hotel_name=hotel_name,
                          hotel_location=hotel_location,
                          hotel_state=hotel_state,
                          hotel_city=hotel_city,
                          hotel_country=hotel_country,
                          hotel_contact=hotel_contact,
                          hotel_star=hotel_star,
                          hotels_card_number=hotels_card_number)

    return {"status": 1, "message": result}


@hotel.post('/add_apartment')
async def add_apartment_api(hotel_id: str,
                            apartments_number: int,
                            room_numbers: int,
                            room_amenity: str,
                            apartment_price: float,
                            status: bool):
    result = add_apartment_db(hotel_id=hotel_id,
                              apartments_number=apartments_number,
                              room_numbers=room_numbers,
                              room_amenity=room_amenity,
                              apartment_price=apartment_price,
                              status=status)
    return {"status": 1, "message": result}


@hotel.delete("/delete_hotel")
async def delete_hotel(hotel_id: int):
    result = delete_hotel_db(hotel_id=hotel_id)
    return result


@hotel.delete("/delete_apartment")
async def delete_apartment(apartment_number: int):
    result = delete_apartment_db(apartments_number=apartment_number)
    return result


@hotel.get("/get_hotel")
async def get_hotels():
    result = get_hotels_db()
    return result


@hotel.get("/get_apartments")
async def get_apartments(hotel_id: int):
    result = get_apartments_db(hotel_id=hotel_id)
    return result
