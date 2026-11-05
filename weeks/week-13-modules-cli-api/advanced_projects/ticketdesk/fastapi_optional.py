"""Optional localhost-only FastAPI teaching adapter.

Install FastAPI/uvicorn separately. Not required by Week 13 checks.
No authentication: NEVER expose publicly or use real customer records.
"""

from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import service, storage

app = FastAPI(title="Ticket Desk educational API")
DB = Path(os.environ.get("TICKETDESK_DB", "tickets.json"))


class CreateTicket(BaseModel):
    title: str = Field(min_length=1)
    priority: str = "normal"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "local-demo"}


@app.get("/tickets")
def list_tickets() -> list[dict]:
    return storage.load_tickets(DB)


@app.post("/tickets", status_code=201)
def create_ticket(payload: CreateTicket) -> dict:
    try:
        updated = service.add_ticket(
            storage.load_tickets(DB), payload.title, payload.priority
        )
        storage.save_tickets(DB, updated)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    return updated[-1]


@app.post("/tickets/{ticket_id}/close")
def close_ticket(ticket_id: int) -> dict:
    current = storage.load_tickets(DB)
    if service.find_ticket(current, ticket_id) is None:
        raise HTTPException(status_code=404, detail="ticket not found")
    try:
        updated = service.close_ticket(current, ticket_id)
        storage.save_tickets(DB, updated)
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error)) from error
    result = service.find_ticket(updated, ticket_id)
    assert result is not None
    return result
