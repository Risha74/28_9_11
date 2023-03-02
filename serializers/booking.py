import typing as t
from datetime import datetime
from pydantic import BaseModel, Field



class BodyToken(BaseModel):
    username: str = Field(...)
    password: str = Field(...)


class BodyBookingIds(BaseModel):
    firstname: str = Field(None)
    lastname: str = Field(None)
    checkin: str = Field(None)
    checkout: str = Field(None)


class BookingDates(BaseModel):
    checkin: datetime = Field(...)
    checkout: datetime = Field(...)


class BodyCreateBooking(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    totalprice: int = Field(...)
    depositpaid: bool = Field(...)
    bookingdates: t.List[BookingDates] = Field(..., min_items=1)
    additionalneeds: str = Field(...)

class ParamGetBooking(BaseModel):
    id: str = Field(...)

