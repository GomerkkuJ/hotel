from database.models import Card, User, Password
from database import get_db


# User Registration
def register_user_db(user_phone_number: int,
                     user_name: str,
                     password: str,
                     user_email: str):
    db = next(get_db())
    checker = db.query(User).filter_by(user_email=user_email).first()
    if checker:
        return "Guest with such number already exist"
    new_user = User(user_phone_number=user_phone_number, user_email=user_email, user_name=user_name)
    db.add(new_user)
    db.commit()
    new_user_password = Password(user_id=new_user.user_id, password=password)
    db.add(new_user_password)
    db.commit()
    return {"message": "Guest Successfully added", "user_id": new_user.user_id}


# Check Password
def check_password_db(user_email, password):
    db = next(get_db())

    cheker1 = db.query(User).filter_by(user_email=user_email).first()

    try:
        cheker2 = db.query(Password).filter_by(user_id=cheker1.user_id).first()

    except:

        cheker2 = False

    if cheker1 and cheker2.password == password:
        return cheker2.user_id

    if cheker1 != user_email:
        return "Wrong email"

    if cheker2.password != password:
        return "Wrong password"


def delete_user_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        db.delete(user)
        db.commit()
        return "User successfully deleted"
    else:
        return "User not found"



def get_user_cabinet_db(user_id):
    db = next(get_db())
    cheker = db.query(User).filter_by(user_id=user_id).first()
    if cheker:
        return cheker
    return "Error"


def get_user_card_db(user_id):
    db = next(get_db())
    cheker = db.query(Card).filter_by(user_id=user_id).first()
    if cheker:
        return cheker
    return "No such card connected"
