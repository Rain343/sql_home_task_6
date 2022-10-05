import sqlalchemy
import json
import os
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

DB_LOGIN = 'rain'
DB_PASSWORD = 'Rain343'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_DATABASE = 'netology'
JSON_FILENAME = 'tests_data.json'
JSON_PATH = os.path.join(os.getcwd(), JSON_FILENAME)

DSN = f'postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
engine = sqlalchemy.create_engine(DSN)


create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open(JSON_PATH, 'r') as f:
    data = json.load(f)
    
    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()


if __name__ == '__main__':

    publisher = Publisher()

    publisher_id = input('Введите id издателя: ')
    find_publisher = session.query(Publisher).filter(Publisher.id == publisher_id).first()

    print(find_publisher)

session.close()