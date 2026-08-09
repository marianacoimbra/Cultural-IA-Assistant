from typing import Dict, List


def get_mock_profile() -> Dict[str, object]:
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Mariana Coimbra",
        "username": "marianacoimbra",
        "bio": "Entusiasta de cultura e assistentes inteligentes.",
        "email": "mariana@example.com",
        "location": "São Paulo, Brasil",
        "website": "https://marianacoimbra.dev",
        "social": {
            "twitter": "@marianacoimbra",
            "linkedin": "linkedin.com/in/marianacoimbra",
            "github": "github.com/marianacoimbra",
        },
        "preferences": {
            "language": "pt-BR",
            "timezone": "America/Sao_Paulo",
            "newsletter": True,
        },
    }


def get_mock_recommendations() -> List[Dict[str, object]]:
    return [
        {
            "id": "rec-001",
            "title": "Museu do Amanhã",
            "category": "Cultura",
            "description": "Uma experiência imersiva sobre ciência, arte e sustentabilidade no Rio de Janeiro.",
            "location": "Rio de Janeiro, Brasil",
            "recommended_for": ["história", "tecnologia", "meio ambiente"],
        },
        {
            "id": "rec-002",
            "title": "Exposição de Arte Contemporânea",
            "category": "Exposição",
            "description": "Mostra com artistas emergentes brasileiros e latinos.",
            "location": "São Paulo, Brasil",
            "recommended_for": ["arte", "cultura brasileira", "design"],
        },
        {
            "id": "rec-003",
            "title": "Roteiro Literário pela Avenida Paulista",
            "category": "Roteiro",
            "description": "Passeio guiado pelos principais pontos literários e saraus da região.",
            "location": "São Paulo, Brasil",
            "recommended_for": ["literatura", "cultura urbana", "eventos"],
        },
    ]

