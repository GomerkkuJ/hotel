from database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, BIGINT, DATE
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'guests'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_phone_number = Column(BIGINT, nullable=False)
    user_email = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    user_reg_date = Column(DateTime, default=datetime.now())


class Password(Base):
    __tablename__ = 'passwords'
    password_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(
        Integer, ForeignKey(column='guests.user_id', ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    password = Column(String, nullable=False)

    user_fk = relationship(User)


class Card(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(
        Integer, ForeignKey('guests.user_id', ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    card_number = Column(Integer, nullable=False)
    card_name = Column(String)
    card_holder = Column(String)
    card_exp_date = Column(Integer, nullable=False)
    card_balance = Column(Float)
    card_added_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User)


class Hotel(Base):
    __tablename__ = 'hotels'
    hotel_id = Column(Integer, autoincrement=True, primary_key=True)
    hotel_name = Column(String, nullable=False)
    hotel_location = Column(String, nullable=False)
    hotel_state = Column(String, nullable=False)
    hotel_city = Column(String, nullable=False)
    hotel_country = Column(String, nullable=False)
    hotel_contact = Column(String)
    hotel_star = Column(Integer)
    hotels_card_number = Column(Integer, nullable=False)


class Apartments(Base):
    __tablename__ = 'apartments'
    apartments_number = Column(Integer, autoincrement=True, primary_key=True)
    hotel_id = Column(
        Integer, ForeignKey(
            'hotels.hotel_id', ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    room_numbers = Column(Integer, nullable=False)
    room_amenity = Column(String, nullable=False)
    apartment_price = Column(Float, nullable=False)
    status = Column(Boolean, nullable=False)

    hotel_fk = relationship(Hotel)


class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, autoincrement=True, primary_key=True)
    card_from = Column(
        Integer, ForeignKey('cards.card_id', ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    amount = Column(Float, nullable=False)
    card_to = Column(
        Integer, ForeignKey('hotels.hotel_id', ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    tansaction_date = Column(DateTime, default=datetime.now())

    card_fk = relationship(Card)
    hotel_fk = relationship(Hotel)


class BookingForm(Base):
    __tablename__ = 'booking'
    booking_id = Column(Integer, autoincrement=True, primary_key=True)
    apartment_id = Column(Integer, nullable=False)
    check_in = Column(DATE, nullable=False)
    check_out = Column(DATE, nullable=False)
    user_id = Column(
        Integer, ForeignKey('guests.user_id', ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )

    user_fk = relationship(User)
