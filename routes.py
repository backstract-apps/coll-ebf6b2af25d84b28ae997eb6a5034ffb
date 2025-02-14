from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/parking_transactions/')
async def get_parking_transactions(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_transactions(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_transactions/id')
async def get_parking_transactions_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_transactions_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_transactions/')
async def post_parking_transactions(raw_data: schemas.PostParkingTransactions, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_transactions(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_transactions/id/')
async def put_parking_transactions_id(raw_data: schemas.PutParkingTransactionsId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_transactions_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_transactions/id')
async def delete_parking_transactions_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_transactions_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_user/')
async def get_parking_user(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_user(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_user/id')
async def get_parking_user_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_user_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_user/')
async def post_parking_user(raw_data: schemas.PostParkingUser, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_user(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_user/id/')
async def put_parking_user_id(raw_data: schemas.PutParkingUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_user_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_user/id')
async def delete_parking_user_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_user_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_lots/')
async def get_parking_lots(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_lots(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_lots/id')
async def get_parking_lots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_lots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_lots/')
async def post_parking_lots(raw_data: schemas.PostParkingLots, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_lots(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_lots/id/')
async def put_parking_lots_id(raw_data: schemas.PutParkingLotsId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_lots_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_lots/id')
async def delete_parking_lots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_lots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parkings_slot/')
async def get_parkings_slot(db: Session = Depends(get_db)):
    try:
        return await service.get_parkings_slot(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parkings_slot/id')
async def get_parkings_slot_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parkings_slot_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parkings_slot/')
async def post_parkings_slot(raw_data: schemas.PostParkingsSlot, db: Session = Depends(get_db)):
    try:
        return await service.post_parkings_slot(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parkings_slot/id/')
async def put_parkings_slot_id(raw_data: schemas.PutParkingsSlotId, db: Session = Depends(get_db)):
    try:
        return await service.put_parkings_slot_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parkings_slot/id')
async def delete_parkings_slot_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parkings_slot_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicles/')
async def get_vehicles(db: Session = Depends(get_db)):
    try:
        return await service.get_vehicles(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicles/id')
async def get_vehicles_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_vehicles_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/vehicles/')
async def post_vehicles(raw_data: schemas.PostVehicles, db: Session = Depends(get_db)):
    try:
        return await service.post_vehicles(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/vehicles/id/')
async def put_vehicles_id(raw_data: schemas.PutVehiclesId, db: Session = Depends(get_db)):
    try:
        return await service.put_vehicles_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/vehicles/id')
async def delete_vehicles_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_vehicles_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/userlogin')
async def post_userlogin(raw_data: schemas.PostUserlogin, db: Session = Depends(get_db)):
    try:
        return await service.post_userlogin(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user/parking_lot')
async def post_user_parking_lot(raw_data: schemas.PostUserParkingLot, db: Session = Depends(get_db)):
    try:
        return await service.post_user_parking_lot(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user/getallparkinglot')
async def get_user_getallparkinglot(db: Session = Depends(get_db)):
    try:
        return await service.get_user_getallparkinglot(db)
    except Exception as e:
        raise HTTPException(500, str(e))

