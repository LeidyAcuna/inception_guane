"""Extra data types
    run: uvicorn example7:app
"""
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from fastapi import Body, FastAPI

app = FastAPI()

class Item(BaseModel):
    item_id: UUID
    start_datetime: Optional[datetime] = Body(None)
    end_datetime: Optional[datetime] = Body(None)
    repeat_at: Optional[time] = Body(None)
    process_after: Optional[timedelta] = Body(None)

@app.put("/items/{item_id}")
async def read_items(item: Item):
    start_process: start_datetime + process_after
    duration: end_datetime - start_process
    
    results = {
        "item": item,
        "start_process": start_process,
        "duration": duration}
    return results
