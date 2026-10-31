"""Ticket Desk: course-local ticket tracker inspired by catalog project 01."""

from .service import add_ticket, close_ticket, find_ticket, summarize

__all__ = ["add_ticket", "close_ticket", "find_ticket", "summarize"]
