from pydantic import BaseModel


class EventLocation(BaseModel):
    latitude: float
    longitude: float


class TicketmasterEvent(BaseModel):
    id: str
    name: str
    url: str | None = None
    date: str | None = None
    venue_name: str | None = None
    location: EventLocation | None = None