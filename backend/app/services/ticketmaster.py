import httpx
from fastapi import HTTPException

from core.config import settings
from schemas.ticketmaster import EventLocation, TicketmasterEvent


class TicketmasterService:
    def __init__(self) -> None:
        self.base_url = settings.ticketmaster_base_url
        self.api_key = settings.ticketmaster_api_key

    async def buscar_eventos_proximos(
        self,
        latitude: float,
        longitude: float,
        raio_km: int = 20,
        tamanho: int = 20,
    ) -> list[TicketmasterEvent]:
        params = {
            "apikey": self.api_key,
            "latlong": f"{latitude},{longitude}",
            "radius": raio_km,
            "unit": "km",
            "size": tamanho,
            "sort": "distance,asc",
            "locale": "pt-br",
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    f"{self.base_url}/events.json",
                    params=params,
                )
                response.raise_for_status()

        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Falha na Ticketmaster: {exc.response.status_code}",
            ) from exc
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=503,
                detail="Não foi possível comunicar com a Ticketmaster.",
            ) from exc

        eventos = response.json().get("_embedded", {}).get("events", [])

        return [
            TicketmasterEvent(
                id=evento["id"],
                name=evento["name"],
                url=evento.get("url"),
                date=evento.get("dates", {}).get("start", {}).get("localDate"),
                venue_name=evento.get("_embedded", {})
                    .get("venues", [{}])[0]
                    .get("name"),
                location=self._extrair_localizacao(evento),
            )
            for evento in eventos
        ]

    @staticmethod
    def _extrair_localizacao(evento: dict) -> EventLocation | None:
        venue = evento.get("_embedded", {}).get("venues", [{}])[0]
        location = venue.get("location")

        if not location:
            return None

        return EventLocation(
            latitude=float(location["latitude"]),
            longitude=float(location["longitude"]),
        )