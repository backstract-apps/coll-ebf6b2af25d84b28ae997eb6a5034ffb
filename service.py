from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_parking_transactions(db: Session):

    parking_transactions_all = db.query(models.ParkingTransactions).all()
    parking_transactions_all = [new_data.to_dict() for new_data in parking_transactions_all] if parking_transactions_all else parking_transactions_all

    res = {
        'parking_transactions_all': parking_transactions_all,
    }
    return res

async def get_parking_transactions_id(db: Session, id: int):

    parking_transactions_one = db.query(models.ParkingTransactions).filter(models.ParkingTransactions.id == id).first() 
    parking_transactions_one = parking_transactions_one.to_dict() if parking_transactions_one else parking_transactions_one

    res = {
        'parking_transactions_one': parking_transactions_one,
    }
    return res

async def post_parking_transactions(db: Session, raw_data: schemas.PostParkingTransactions):
    id:str = raw_data.id
    vehicle_id:str = raw_data.vehicle_id
    slot_id:str = raw_data.slot_id
    check_in:str = raw_data.check_in
    check_out:str = raw_data.check_out
    total_fee:str = raw_data.total_fee


    record_to_be_added = {'id': id, 'vehicle_id': vehicle_id, 'slot_id': slot_id, 'check_in': check_in, 'check_out': check_out, 'total_fee': total_fee}
    new_parking_transactions = models.ParkingTransactions(**record_to_be_added)
    db.add(new_parking_transactions)
    db.commit()
    db.refresh(new_parking_transactions)
    parking_transactions_inserted_record = new_parking_transactions.to_dict()

    res = {
        'parking_transactions_inserted_record': parking_transactions_inserted_record,
    }
    return res

async def put_parking_transactions_id(db: Session, raw_data: schemas.PutParkingTransactionsId):
    id:str = raw_data.id
    vehicle_id:str = raw_data.vehicle_id
    slot_id:str = raw_data.slot_id
    check_in:str = raw_data.check_in
    check_out:str = raw_data.check_out
    total_fee:str = raw_data.total_fee


    parking_transactions_edited_record = db.query(models.ParkingTransactions).filter(models.ParkingTransactions.id == id).first()
    for key, value in {'id': id, 'vehicle_id': vehicle_id, 'slot_id': slot_id, 'check_in': check_in, 'check_out': check_out, 'total_fee': total_fee}.items():
          setattr(parking_transactions_edited_record, key, value)
    db.commit()
    db.refresh(parking_transactions_edited_record)
    parking_transactions_edited_record = parking_transactions_edited_record.to_dict() 

    res = {
        'parking_transactions_edited_record': parking_transactions_edited_record,
    }
    return res

async def delete_parking_transactions_id(db: Session, id: int):

    parking_transactions_deleted = None
    record_to_delete = db.query(models.ParkingTransactions).filter(models.ParkingTransactions.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_transactions_deleted = record_to_delete.to_dict() 

    res = {
        'parking_transactions_deleted': parking_transactions_deleted,
    }
    return res

async def get_parking_user(db: Session):

    parking_user_all = db.query(models.ParkingUser).all()
    parking_user_all = [new_data.to_dict() for new_data in parking_user_all] if parking_user_all else parking_user_all

    res = {
        'parking_user_all': parking_user_all,
    }
    return res

async def get_parking_user_id(db: Session, id: int):

    parking_user_one = db.query(models.ParkingUser).filter(models.ParkingUser.id == id).first() 
    parking_user_one = parking_user_one.to_dict() if parking_user_one else parking_user_one

    res = {
        'parking_user_one': parking_user_one,
    }
    return res

async def post_parking_user(db: Session, raw_data: schemas.PostParkingUser):
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password
    id:int = raw_data.id


    import datetime

    try:
        created_at = datetime.datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': id, 'name': name, 'email': email, 'password': password, 'created_at': created_at}
    new_parking_user = models.ParkingUser(**record_to_be_added)
    db.add(new_parking_user)
    db.commit()
    db.refresh(new_parking_user)
    parking_user_inserted_record = new_parking_user.to_dict()

    res = {
        'parking_user_inserted_record': parking_user_inserted_record,
    }
    return res

async def put_parking_user_id(db: Session, raw_data: schemas.PutParkingUserId):
    id:str = raw_data.id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password
    created_at:str = raw_data.created_at


    parking_user_edited_record = db.query(models.ParkingUser).filter(models.ParkingUser.id == id).first()
    for key, value in {'id': id, 'name': name, 'email': email, 'password': password, 'created_at': created_at}.items():
          setattr(parking_user_edited_record, key, value)
    db.commit()
    db.refresh(parking_user_edited_record)
    parking_user_edited_record = parking_user_edited_record.to_dict() 

    res = {
        'parking_user_edited_record': parking_user_edited_record,
    }
    return res

async def delete_parking_user_id(db: Session, id: int):

    parking_user_deleted = None
    record_to_delete = db.query(models.ParkingUser).filter(models.ParkingUser.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_user_deleted = record_to_delete.to_dict() 

    res = {
        'parking_user_deleted': parking_user_deleted,
    }
    return res

async def get_parking_lots(db: Session):

    parking_lots_all = db.query(models.ParkingLots).all()
    parking_lots_all = [new_data.to_dict() for new_data in parking_lots_all] if parking_lots_all else parking_lots_all

    res = {
        'parking_lots_all': parking_lots_all,
    }
    return res

async def get_parking_lots_id(db: Session, id: int):

    parking_lots_one = db.query(models.ParkingLots).filter(models.ParkingLots.id == id).first() 
    parking_lots_one = parking_lots_one.to_dict() if parking_lots_one else parking_lots_one

    res = {
        'parking_lots_one': parking_lots_one,
    }
    return res

async def post_parking_lots(db: Session, raw_data: schemas.PostParkingLots):
    id:str = raw_data.id
    user_id:str = raw_data.user_id
    name:str = raw_data.name
    location:str = raw_data.location
    capacity:str = raw_data.capacity
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'user_id': user_id, 'name': name, 'location': location, 'capacity': capacity, 'created_at': created_at}
    new_parking_lots = models.ParkingLots(**record_to_be_added)
    db.add(new_parking_lots)
    db.commit()
    db.refresh(new_parking_lots)
    parking_lots_inserted_record = new_parking_lots.to_dict()

    res = {
        'parking_lots_inserted_record': parking_lots_inserted_record,
    }
    return res

async def put_parking_lots_id(db: Session, raw_data: schemas.PutParkingLotsId):
    id:str = raw_data.id
    user_id:str = raw_data.user_id
    name:str = raw_data.name
    location:str = raw_data.location
    capacity:str = raw_data.capacity
    created_at:str = raw_data.created_at


    parking_lots_edited_record = db.query(models.ParkingLots).filter(models.ParkingLots.id == id).first()
    for key, value in {'id': id, 'user_id': user_id, 'name': name, 'location': location, 'capacity': capacity, 'created_at': created_at}.items():
          setattr(parking_lots_edited_record, key, value)
    db.commit()
    db.refresh(parking_lots_edited_record)
    parking_lots_edited_record = parking_lots_edited_record.to_dict() 

    res = {
        'parking_lots_edited_record': parking_lots_edited_record,
    }
    return res

async def delete_parking_lots_id(db: Session, id: int):

    parking_lots_deleted = None
    record_to_delete = db.query(models.ParkingLots).filter(models.ParkingLots.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_lots_deleted = record_to_delete.to_dict() 

    res = {
        'parking_lots_deleted': parking_lots_deleted,
    }
    return res

async def get_parkings_slot(db: Session):

    parkings_slot_all = db.query(models.ParkingsSlot).all()
    parkings_slot_all = [new_data.to_dict() for new_data in parkings_slot_all] if parkings_slot_all else parkings_slot_all

    res = {
        'parkings_slot_all': parkings_slot_all,
    }
    return res

async def get_parkings_slot_id(db: Session, id: int):

    parkings_slot_one = db.query(models.ParkingsSlot).filter(models.ParkingsSlot.id == id).first() 
    parkings_slot_one = parkings_slot_one.to_dict() if parkings_slot_one else parkings_slot_one

    res = {
        'parkings_slot_one': parkings_slot_one,
    }
    return res

async def post_parkings_slot(db: Session, raw_data: schemas.PostParkingsSlot):
    id:str = raw_data.id
    lot_id:str = raw_data.lot_id
    slot_number:str = raw_data.slot_number
    type:str = raw_data.type
    hourly_rate:str = raw_data.hourly_rate
    is_occupied:str = raw_data.is_occupied
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'lot_id': lot_id, 'slot_number': slot_number, 'type': type, 'hourly_rate': hourly_rate, 'is_occupied': is_occupied, 'created_at': created_at}
    new_parkings_slot = models.ParkingsSlot(**record_to_be_added)
    db.add(new_parkings_slot)
    db.commit()
    db.refresh(new_parkings_slot)
    parkings_slot_inserted_record = new_parkings_slot.to_dict()

    res = {
        'parkings_slot_inserted_record': parkings_slot_inserted_record,
    }
    return res

async def put_parkings_slot_id(db: Session, raw_data: schemas.PutParkingsSlotId):
    id:str = raw_data.id
    lot_id:str = raw_data.lot_id
    slot_number:str = raw_data.slot_number
    type:str = raw_data.type
    hourly_rate:str = raw_data.hourly_rate
    is_occupied:str = raw_data.is_occupied
    created_at:str = raw_data.created_at


    parkings_slot_edited_record = db.query(models.ParkingsSlot).filter(models.ParkingsSlot.id == id).first()
    for key, value in {'id': id, 'lot_id': lot_id, 'slot_number': slot_number, 'type': type, 'hourly_rate': hourly_rate, 'is_occupied': is_occupied, 'created_at': created_at}.items():
          setattr(parkings_slot_edited_record, key, value)
    db.commit()
    db.refresh(parkings_slot_edited_record)
    parkings_slot_edited_record = parkings_slot_edited_record.to_dict() 

    res = {
        'parkings_slot_edited_record': parkings_slot_edited_record,
    }
    return res

async def delete_parkings_slot_id(db: Session, id: int):

    parkings_slot_deleted = None
    record_to_delete = db.query(models.ParkingsSlot).filter(models.ParkingsSlot.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parkings_slot_deleted = record_to_delete.to_dict() 

    res = {
        'parkings_slot_deleted': parkings_slot_deleted,
    }
    return res

async def get_vehicles(db: Session):

    vehicles_all = db.query(models.Vehicles).all()
    vehicles_all = [new_data.to_dict() for new_data in vehicles_all] if vehicles_all else vehicles_all

    res = {
        'vehicles_all': vehicles_all,
    }
    return res

async def get_vehicles_id(db: Session, id: int):

    vehicles_one = db.query(models.Vehicles).filter(models.Vehicles.id == id).first() 
    vehicles_one = vehicles_one.to_dict() if vehicles_one else vehicles_one

    res = {
        'vehicles_one': vehicles_one,
    }
    return res

async def post_vehicles(db: Session, raw_data: schemas.PostVehicles):
    id:str = raw_data.id
    lot_id:str = raw_data.lot_id
    registration_id:str = raw_data.registration_id
    owner_name:str = raw_data.owner_name
    phone_number:str = raw_data.phone_number
    model_type:str = raw_data.model_type
    color:str = raw_data.color
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'lot_id': lot_id, 'registration_id': registration_id, 'owner_name': owner_name, 'phone_number': phone_number, 'model_type': model_type, 'color': color, 'created_at': created_at}
    new_vehicles = models.Vehicles(**record_to_be_added)
    db.add(new_vehicles)
    db.commit()
    db.refresh(new_vehicles)
    vehicles_inserted_record = new_vehicles.to_dict()

    res = {
        'vehicles_inserted_record': vehicles_inserted_record,
    }
    return res

async def put_vehicles_id(db: Session, raw_data: schemas.PutVehiclesId):
    id:str = raw_data.id
    lot_id:str = raw_data.lot_id
    registration_id:str = raw_data.registration_id
    owner_name:str = raw_data.owner_name
    phone_number:str = raw_data.phone_number
    model_type:str = raw_data.model_type
    color:str = raw_data.color
    created_at:str = raw_data.created_at


    vehicles_edited_record = db.query(models.Vehicles).filter(models.Vehicles.id == id).first()
    for key, value in {'id': id, 'lot_id': lot_id, 'registration_id': registration_id, 'owner_name': owner_name, 'phone_number': phone_number, 'model_type': model_type, 'color': color, 'created_at': created_at}.items():
          setattr(vehicles_edited_record, key, value)
    db.commit()
    db.refresh(vehicles_edited_record)
    vehicles_edited_record = vehicles_edited_record.to_dict() 

    res = {
        'vehicles_edited_record': vehicles_edited_record,
    }
    return res

async def delete_vehicles_id(db: Session, id: int):

    vehicles_deleted = None
    record_to_delete = db.query(models.Vehicles).filter(models.Vehicles.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        vehicles_deleted = record_to_delete.to_dict() 

    res = {
        'vehicles_deleted': vehicles_deleted,
    }
    return res

async def post_userlogin(db: Session, raw_data: schemas.PostUserlogin):
    email:str = raw_data.email
    password:str = raw_data.password


    user_data = db.query(models.ParkingUser).filter(models.ParkingUser.email == email).count() > 0

    user_datas = db.query(models.ParkingUser).filter(models.ParkingUser.password == password).first() 
    user_datas = user_datas.to_dict() if user_datas else user_datas

    res = {
        'user_data': user_data,
    }
    return res

async def post_user_parking_lot(db: Session, raw_data: schemas.PostUserParkingLot):
    id:int = raw_data.id
    user_id:int = raw_data.user_id
    name:str = raw_data.name
    location:str = raw_data.location
    capacity:int = raw_data.capacity


    import datetime

    try:
        created_at = datetime.datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'name': name, 'location': location, 'user_id': user_id, 'id': id, 'capacity': capacity}
    new_parking_lots = models.ParkingLots(**record_to_be_added)
    db.add(new_parking_lots)
    db.commit()
    db.refresh(new_parking_lots)
    user_parking_lot_data = new_parking_lots.to_dict()

    res = {
        'user_parking_lot_data': user_parking_lot_data,
    }
    return res

async def get_user_getallparkinglot(db: Session):

    user_parking_lot_data = db.query(models.ParkingLots).all()
    user_parking_lot_data = [new_data.to_dict() for new_data in user_parking_lot_data] if user_parking_lot_data else user_parking_lot_data

    res = {
        'user_parking_lot_data': user_parking_lot_data,
    }
    return res

