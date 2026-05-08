from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from services.order_service.database import Base, engine, SessionLocal
from services.order_service.models import Order

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Service")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Order Service Running"}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "order_service"}


@app.post("/orders")
def create_order(
    user_id: int,
    item_name: str,
    quantity: int,
    total_price: float,
    db: Session = Depends(get_db)
):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than zero")

    if total_price <= 0:
        raise HTTPException(status_code=400, detail="Total price must be greater than zero")

    order = Order(
        user_id=user_id,
        item_name=item_name,
        quantity=quantity,
        total_price=total_price,
        status="CREATED"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return {
        "id": order.id,
        "user_id": order.user_id,
        "item_name": order.item_name,
        "quantity": order.quantity,
        "total_price": order.total_price,
        "status": order.status
    }


@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()

    return [
        {
            "id": order.id,
            "user_id": order.user_id,
            "item_name": order.item_name,
            "quantity": order.quantity,
            "total_price": order.total_price,
            "status": order.status
        }
        for order in orders
    ]


@app.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "id": order.id,
        "user_id": order.user_id,
        "item_name": order.item_name,
        "quantity": order.quantity,
        "total_price": order.total_price,
        "status": order.status
    }