from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import httpx

from utils.mock import get_profile

router = APIRouter()

class Profile(BaseModel):
    name: str
    preferences: list[str]
    subpreferences: list[str]
    age: int
    geolocation: str


@router.get("/profile")
async def get_profile_route():
    return get_profile()

@router.post("/profile")
async def create_profile_route(profile: Profile):
    # Here you would typically save the profile to a database (TODO: Implement database saving logic)
    return {"message": "Profile created successfully", "profile": profile}

@router.post("/profile/location")
async def receive_location(location: str):
    # TODO: pegar loc a partir do frontend e salvar no banco de dados (ainda não implementado)
    return {"message": "Location received successfully", "location": location}

@router.get("/profile/ip-location")
async def get_ip_location():
    mock_data = {
    "ip": "2804:14c:16b:8405:591b:708:3e4f:1f88",
    "network": "2804:14c:16b::/48",
    "version": "IPv6",
    "city": "Caieiras",
    "region": "Sao Paulo",
    "region_code": "SP",
    "country": "BR",
    "country_name": "Brazil",
    "country_code": "BR",
    "country_code_iso3": "BRA",
    "country_capital": "Brasilia",
    "country_tld": ".br",
    "continent_code": "SA",
    "in_eu": "false",
    "postal": "07700-000",
    "latitude": -23.44859,
    "longitude": -46.68839,
    "timezone": "America/Sao_Paulo",
    "utc_offset": "-0300",
    "country_calling_code": "+55",
    "currency": "BRL",
    "currency_name": "Real",
    "languages": "pt-BR,es,en,fr",
    "country_area": 8511965.0,
    "country_population": 209469333,
    "asn": "AS28573",
    "org": "Claro NXT Telecomunicacoes Ltda"
}
    return {
        "city": mock_data.get("city"),
        "latitude": mock_data.get("latitude"),
        "longitude": mock_data.get("longitude"),
        "source": "local_ipapi.co",
    }