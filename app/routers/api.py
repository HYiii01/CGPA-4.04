from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from app.schemas import FlightDelayRequest, FlightStatusWebhook, LocationUpdate, VoteRequest
from app.services.trip_service import (
    analyze_flight_delay as analyze_delay,
    cast_vote as add_vote,
    get_flight_status as read_flight_status,
    get_votes as read_votes,
    update_flight_status,
)

router = APIRouter(prefix="/api")

_locations = {
    "Ryan": {"member": "Ryan", "latitude": 3.1579, "longitude": 101.7123, "status": "sharing", "updated_at": None},
    "Marcus": {"member": "Marcus", "latitude": 3.1588, "longitude": 101.7111, "status": "sharing", "updated_at": None},
    "Aina": {"member": "Aina", "latitude": 3.1558, "longitude": 101.7142, "status": "last seen 2 min ago", "updated_at": None},
}


@router.get("/ai/flight-status")
def get_flight_status():
    return read_flight_status()


@router.post("/webhooks/flight-status")
def receive_flight_status(update: FlightStatusWebhook):
    flight = update_flight_status(update.flight_number, update.status, update.delay_minutes)
    return {"received": True, "flight": flight}


@router.post("/ai/flight-delay")
def analyze_flight_delay(flight: FlightDelayRequest):
    return analyze_delay(flight.flight_number, flight.delay_minutes)


@router.get("/votes")
def get_votes():
    return read_votes()


@router.post("/votes")
def cast_vote(vote: VoteRequest):
    if vote.option_id not in read_votes()["options"]:
        raise HTTPException(status_code=400, detail="Unknown vote option")
    return add_vote(vote.option_id)


@router.get("/locations")
def get_locations():
    return {"locations": list(_locations.values())}


@router.post("/locations")
def update_location(location: LocationUpdate):
    if location.member not in _locations:
        raise HTTPException(status_code=400, detail="Unknown trip member")
    _locations[location.member] = {
        **location.model_dump(),
        "status": "sharing",
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    return {"locations": list(_locations.values())}
