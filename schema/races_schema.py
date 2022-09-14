from pydantic import BaseModel
from typing import Optional

class RacesSchema(BaseModel):
    'raceId' : int
    'year' : int
    'round' : int
    'circuitId' : int
    'name' : str
    'date' : str
    'time' : str
    'url' : str