"""Safe re-export for inbound adapters."""
import importlib

_mod = importlib.import_module("infrastructure.adapter.in.request_controller")
BugController = _mod.BugController

__all__ = ["BugController"]
