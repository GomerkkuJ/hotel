import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="asd54321",
                              host="localhost",
                              database="hotel")
sql = connection.cursor()

def add_guest(user_id, user_name,  user_phone_number, user_email,  user_reg_date):
    # Create/login to database
    connection = psycopg2.connect("hotel.db")
    # Creating translator
    sql = connection.cursor()
    # Adding user into database
    sql.execute("INSERT INTO sellers VALUES (?, ?, ?, ?, ?);",
                (user_id, user_name,  user_phone_number, user_email,  user_reg_date))