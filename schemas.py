from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class ParkingTransactions(BaseModel):
    id: int
    vehicle_id: int
    slot_id: int
    check_in: datetime.time
    check_out: datetime.time
    total_fee: float


class ReadParkingTransactions(BaseModel):
    id: int
    vehicle_id: int
    slot_id: int
    check_in: datetime.time
    check_out: datetime.time
    total_fee: float
    class Config:
        from_attributes = True


class ParkingUser(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime.time


class ReadParkingUser(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime.time
    class Config:
        from_attributes = True


class ParkingLots(BaseModel):
    id: int
    user_id: int
    name: str
    location: str
    capacity: int
    created_at: datetime.time


class ReadParkingLots(BaseModel):
    id: int
    user_id: int
    name: str
    location: str
    capacity: int
    created_at: datetime.time
    class Config:
        from_attributes = True


class ParkingsSlot(BaseModel):
    id: int
    lot_id: int
    slot_number: int
    type: str
    hourly_rate: float
    is_occupied: bool
    created_at: datetime.time


class ReadParkingsSlot(BaseModel):
    id: int
    lot_id: int
    slot_number: int
    type: str
    hourly_rate: float
    is_occupied: bool
    created_at: datetime.time
    class Config:
        from_attributes = True


class Vehicles(BaseModel):
    id: int
    lot_id: int
    registration_id: str
    owner_name: str
    phone_number: str
    model_type: str
    color: str
    created_at: datetime.time


class ReadVehicles(BaseModel):
    id: int
    lot_id: int
    registration_id: str
    owner_name: str
    phone_number: str
    model_type: str
    color: str
    created_at: datetime.time
    class Config:
        from_attributes = True




class PostParkingTransactions(BaseModel):
    id: str
    vehicle_id: str
    slot_id: str
    check_in: str
    check_out: str
    total_fee: str

    class Config:
        from_attributes = True



class PutParkingTransactionsId(BaseModel):
    id: str
    vehicle_id: str
    slot_id: str
    check_in: str
    check_out: str
    total_fee: str

    class Config:
        from_attributes = True



class PostParkingUser(BaseModel):
    name: str
    email: str
    password: str
    id: int

    class Config:
        from_attributes = True



class PutParkingUserId(BaseModel):
    id: str
    name: str
    email: str
    password: str
    created_at: str

    class Config:
        from_attributes = True



class PostParkingLots(BaseModel):
    id: str
    user_id: str
    name: str
    location: str
    capacity: str
    created_at: str

    class Config:
        from_attributes = True



class PutParkingLotsId(BaseModel):
    id: str
    user_id: str
    name: str
    location: str
    capacity: str
    created_at: str

    class Config:
        from_attributes = True



class PostParkingsSlot(BaseModel):
    id: str
    lot_id: str
    slot_number: str
    type: str
    hourly_rate: str
    is_occupied: str
    created_at: str

    class Config:
        from_attributes = True



class PutParkingsSlotId(BaseModel):
    id: str
    lot_id: str
    slot_number: str
    type: str
    hourly_rate: str
    is_occupied: str
    created_at: str

    class Config:
        from_attributes = True



class PostVehicles(BaseModel):
    id: str
    lot_id: str
    registration_id: str
    owner_name: str
    phone_number: str
    model_type: str
    color: str
    created_at: str

    class Config:
        from_attributes = True



class PutVehiclesId(BaseModel):
    id: str
    lot_id: str
    registration_id: str
    owner_name: str
    phone_number: str
    model_type: str
    color: str
    created_at: str

    class Config:
        from_attributes = True



class PostUserlogin(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True



class PostUserParkingLot(BaseModel):
    id: int
    user_id: int
    name: str
    location: str
    capacity: int

    class Config:
        from_attributes = True

