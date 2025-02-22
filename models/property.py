from pydantic import BaseModel
from typing import List, Optional

class Property(BaseModel):
    """
    Represents the data structure of a Property listing.
    """
    title: str
    property_type: str
    price: str
    location: str
    total_area: Optional[str]
    number_of_floors: Optional[str]
    number_of_bedrooms: Optional[str]
    number_of_bathrooms: Optional[str]
    garage_parking: Optional[str]
    amenities: List[str]
    energy_rating: Optional[str]
    construction_details: Optional[str]
    description: str
    construction_status: Optional[str] 