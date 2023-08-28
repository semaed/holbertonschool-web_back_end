#!/usr/bin/env python3
"""Script takes a float and return multiplier of floats"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates function to multiply"""
    def multiplier_function(d: float) -> float:
        """Retunrs multplier result"""
        return d * multiplier
    return multiplier_function
