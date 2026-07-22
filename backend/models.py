from pydantic import BaseModel
from typing import List, Optional


class UserEvent(BaseModel):
    event_type: str
    product_id: Optional[str] = None
    category: Optional[str] = None
    timestamp: str
    metadata: Optional[dict] = None


class SessionRequest(BaseModel):
    user_id: str
    events: List[UserEvent]