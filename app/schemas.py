from pydantic import BaseModel


class VoteRequest(BaseModel):
    option_id: str


class FlightDelayRequest(BaseModel):
    flight_number: str
    delay_minutes: int


class FlightStatusWebhook(BaseModel):
    flight_number: str
    status: str = "scheduled"
    delay_minutes: int = 0


class LocationUpdate(BaseModel):
    member: str
    latitude: float
    longitude: float
