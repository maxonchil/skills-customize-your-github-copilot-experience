"""
FastAPI Starter Code - Todo API
A basic REST API template to get you started with FastAPI.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="Todo API", version="1.0.0")

# Pydantic model for request/response validation
class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory data store
items_db: List[Item] = []

# TODO: Add your endpoints here
# Example structure:
# @app.get("/items")
# async def get_items():
#     return items_db

# @app.post("/items")
# async def create_item(item: Item):
#     items_db.append(item)
#     return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
