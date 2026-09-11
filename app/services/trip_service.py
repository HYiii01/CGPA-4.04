from typing import Any


VOTE_OPTIONS: dict[str, dict[str, Any]] = {
    "bistro": {"label": "Hameediyah Bistro", "detail": "Nasi Kandar · Campbell St", "votes": 3},
    "restaurant": {"label": "Tek Sen Restaurant", "detail": "Zhi Char · Carnarvon St", "votes": 2},
    "night-market": {"label": "Hin Bus Depot Night Market", "detail": "Art, craft, food stalls", "votes": 2},
    "beach-bar": {"label": "Batu Ferringhi Beach Bar", "detail": "Cocktails, sea breeze", "votes": 1},
}

_latest_flight_status = {
    "flight_number": "AK 6114",
    "status": "scheduled",
    "delay_minutes": 0,
}


def get_votes() -> dict[str, Any]:
    return {
        "options": VOTE_OPTIONS,
        "total_votes": sum(item["votes"] for item in VOTE_OPTIONS.values()),
    }


def cast_vote(option_id: str) -> dict[str, Any]:
    VOTE_OPTIONS[option_id]["votes"] += 1
    return get_votes()


def get_flight_status() -> dict[str, Any]:
    return _latest_flight_status


def update_flight_status(flight_number: str, status: str, delay_minutes: int) -> dict[str, Any]:
    _latest_flight_status.update(
        {
            "flight_number": flight_number.upper(),
            "status": status,
            "delay_minutes": max(0, delay_minutes),
        }
    )
    return _latest_flight_status


def analyze_flight_delay(flight_number: str, delay_minutes: int) -> dict[str, str]:
    delay = max(0, delay_minutes)
    normalized_flight = flight_number.upper()

    if delay == 0:
        return {
            "severity": "clear",
            "message": f"{normalized_flight} is currently on schedule.",
            "recommendation": "Keep the current itinerary and continue monitoring.",
        }
    if delay < 30:
        return {
            "severity": "watch",
            "message": f"{normalized_flight} is delayed by {delay} minutes.",
            "recommendation": "Keep the plan, but move the next transfer buffer forward by 15 minutes.",
        }
    return {
        "severity": "critical",
        "message": f"{normalized_flight} is delayed by {delay} minutes.",
        "recommendation": "Notify the group and let AI re-order the next activity to protect the dinner window.",
    }
