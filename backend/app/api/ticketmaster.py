from fastapi import APIRouter, Query

from app.schemas.ticketmaster import TicketmasterEvent
from app.services.ticketmaster import TicketmasterService

router = APIRouter(prefix="/events", tags=["Eventos"])
ticketmaster_service = TicketmasterService()


@router.get("/proximos", response_model=list[TicketmasterEvent])
async def eventos_proximos(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    raio_km: int = Query(20, ge=1, le=200),
):
    return await ticketmaster_service.buscar_eventos_proximos(
        latitude=latitude,
        longitude=longitude,
        raio_km=raio_km,
    )