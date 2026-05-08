from sqlalchemy import Column, Integer, String, Float
from services.order_service.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    item_name = Column(String)
    quantity = Column(Integer)
    total_price = Column(Float)
    status = Column(String, default="CREATED")