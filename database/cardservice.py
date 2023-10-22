from database.models import Card, User, Transaction
from database import get_db


def add_user_card_to_db(**kwargs):
    db = next(get_db())
    card_number = kwargs.get('card_number')

    checker = db.query(Card).filter_by(card_number=card_number).first()
    if checker:
        return "Card already exist"
    new_card = Card(**kwargs)
    db.add(new_card)
    db.commit()

    return "Card successfully added"


def delete_user_card_db(card_id, user_id):
    db = next(get_db())
    card_delete = db.query(Card).filter_by(user_id=user_id, card_id=card_id).first()
    if card_delete:
        db.delete(card_delete)
        db.commit()
        return "Card deleted"
    return "Wrong inputs"


def get_exact_card_balance_db(card_number):
    db = next(get_db())
    exact_card = db.query(Card).filter_by(card_number=card_number).first()
    if exact_card is None:
        return "Card not found"
    return exact_card.card_balance
