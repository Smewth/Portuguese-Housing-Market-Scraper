# Configuration for the real estate crawler

BASE_URL = "https://www.imovirtual.com/pt/anuncio/t3-remodelado-ao-centro-de-almada-ID1e2X7.html"
CSS_SELECTOR = "div.css-1d9dws4"  # Main container for property details

REQUIRED_KEYS = [
    "title",
    "property_type",
    "price",
    "location",
    "description"
] 