#!/usr/bin/python3
""" LockedClass Module
This module defines the `LockedClass` class 
with restricted attributes using __slots__."""


class LockedClass():
    """LockedClass with restricted attributes."""
    __slots__ = ('first_name',)
