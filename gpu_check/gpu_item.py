from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class GpuItem:
    name: Optional[str] = None
    price: Optional[Decimal] = None
    currency: Optional[str] = None
    year: Optional[str] = None
    memory: Optional[str] = None
    recommended_power_supply: Optional[str] = None
    average_1080p_performance: Optional[str] = None
    average_1440p_performance: Optional[str] = None
    average_4k_performance: Optional[str] = None
