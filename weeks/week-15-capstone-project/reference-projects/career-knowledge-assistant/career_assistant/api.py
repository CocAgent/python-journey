"""Optional FastAPI adapter. Core logic stays independent of HTTP."""

import os
from pathlib import Path

from career_assistant import service


def create_app(db_path: str | Path | None = None):
    """Build an HTTP adapter for local development, with optional dependency."""
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel, Field

    db = Path(db_path or os.environ.get("CAREER_ASSISTANT_DB", "career.db"))
    app = FastAPI(title="Career Knowledge Assistant", version="1.0.0")

    class NoteInput(BaseModel):
        title: str = Field(min_length=1)
        body: str = Field(min_length=1)
        tags: str = ""

    class SkillInput(BaseModel):
        name: str = Field(min_length=1)
        level: int = Field(ge=0, le=5)
        comment: str = ""

    @app.get("/health")
    def health():
        return {"status": "ok", "mode": "local-demo"}

    @app.get("/notes")
    def notes():
        return service.list_notes(db)

    @app.post("/notes", status_code=201)
    def add_note(item: NoteInput):
        try:
            return {"id": service.add_note(db, item.title, item.body, item.tags)}
        except ValueError as error:
            raise HTTPException(status_code=422, detail=str(error)) from error

    @app.get("/search")
    def search(q: str):
        try:
            return service.search_notes(db, q)
        except ValueError as error:
            raise HTTPException(status_code=422, detail=str(error)) from error

    @app.put("/skills")
    def skill(item: SkillInput):
        try:
            service.set_skill(db, item.name, item.level, item.comment)
        except ValueError as error:
            raise HTTPException(status_code=422, detail=str(error)) from error
        return {"updated": item.name}

    @app.get("/skills")
    def skills():
        return service.list_skills(db)

    @app.get("/summary")
    def summary():
        return service.summary(db)

    return app


def __getattr__(name: str):
    """Load the app lazily, so basic CLI use never needs FastAPI installed."""
    if name == "app":
        return create_app()
    raise AttributeError(name)
