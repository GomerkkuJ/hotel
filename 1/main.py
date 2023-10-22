import uvicorn
from fastapi import FastAPI

from booked_rooms.booked_rooms_api import book
from card.card_api import card
from database import Base, engine
from guest.guest_api import guest
from hotel.hotel_api import hotel

Base.metadata.create_all(bind=engine)


def main():
    app = FastAPI(
        app_title="GoldenHouse Hotel booking API Production",
        project_version="0.78.7",
        docs_url="/hotel/api/docs",
        redoc_url="/hotel/api/redoc",
        openapi_url="/hotel/api/openapi.json"
    )
    routers = [card, book, guest, hotel]
    for router in routers:
        app.include_router(router)
    uvicorn.run(app=app, host="localhost", port=7500)


# Start Fast Api
# uvicorn main:app --reload
if __name__ == '__main__':
    main()
