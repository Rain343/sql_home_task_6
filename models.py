import sqlalchemy as db
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Shop(Base):
    __tablename__ = "shop"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), unique=True)


class Stock(Base):
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    id_shop = db.Column(db.Integer, db.ForeignKey("shop.id"), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    
    shop = relationship(Shop, backref="reserves")

    def __str__(self):
        return f'Stock(id: {self.id}, id_book: {self.id_book}, id_shop: {self.id_shop}, count: {self.count})'


class Book(Base):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=40), nullable=False)
    id_publisher = db.Column(db.Integer, db.ForeignKey("publisher.id"), nullable=False)

    stock = relationship(Stock, backref="books")

    def __str__(self):
        return f'Book(id: {self.id}, title: {self.title}, id_publisher: {self.id_publisher})'


class Publisher(Base):
    __tablename__ = "publisher"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), unique=True)

    book = relationship(Book, backref="publishers")

    def __str__(self):
        return f'Publisher(id: {self.id}, name: {self.name})'


class Sale(Base):
    __tablename__ = "sale"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(6), nullable=False)
    date_sale = db.Column(db.DateTime, nullable=False)
    id_stock = db.Column(db.Integer, db.ForeignKey("stock.id"), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    stock = relationship(Stock, backref="sales")


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)