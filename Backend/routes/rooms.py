from typing import List

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from config.database import get_db
from models.models import Room
from routes.units import get_unit
from schemas.room_schema import RoomSchema

rooms = APIRouter()


@rooms.get("/api/rooms", response_model=List[RoomSchema], tags=["locations"])
def get_rooms(db: Session = Depends(get_db)):
    result = db.query(Room).all()
    return result


@rooms.post("/api/rooms", status_code=HTTP_201_CREATED, tags=["locations"])
def add_room(room: RoomSchema, db: Session = Depends(get_db)):
    db_unit = get_unit(room.unit_id, db=db)
    if not db_unit:
        return Response(status_code=HTTP_404_NOT_FOUND)
    new_room = Room(name=room.name, unit_id=room.unit_id)
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    content = str(new_room.id)
    return Response(status_code=HTTP_201_CREATED, content=content)


@rooms.get("/api/room/{room_id}", response_model=RoomSchema, tags=["locations"])
def get_room(room_id: int, db: Session = Depends(get_db)):
    return db.query(Room).filter(Room.id == room_id).first()


@rooms.get("/api/rooms/{unit_id}", response_model=List[RoomSchema], tags=["locations"])
def get_rooms_unit(unit_id: int, db: Session = Depends(get_db)):
    return db.query(Room).filter(Room.unit_id == unit_id).all()


@rooms.put("/api/rooms/{room_id}", response_model=RoomSchema, tags=["locations"])
def update_room(data_update: RoomSchema, room_id: int, db: Session = Depends(get_db)):
    db_room = get_room(room_id, db=db)
    if not db_room:
        return Response(status_code=HTTP_404_NOT_FOUND)
    for key, value in data_update.model_dump(exclude_unset=True).items():
        setattr(db_room, key, value)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


@rooms.delete("/api/rooms/{room_id}", status_code=HTTP_204_NO_CONTENT, tags=["locations"])
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = get_room(room_id, db=db)
    if not db_room:
        return Response(status_code=HTTP_404_NOT_FOUND)
    db.delete(db_room)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
