from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass(frozen=True)
class OrderedLine:
    order_id: str
    sku: str
    quantity: int


class Batch:
    """
    Model domain
    """

    def __init__(
            self,
            reference: str,
            sku: str,
            qty: int,
            eta: Optional[date]
    ):
        self.reference = reference
        self.sku = sku
        self._purchased_qty = qty
        self.eta = eta
        self._allocations = set()

    def allocate(self, order: OrderedLine):
        if self.can_allocate(order):
            self._allocations.add(order)

    def deallocate(self, order: OrderedLine):
        if order in self._allocations:
            self._allocations.remove(order)

    @property
    def allocated_quantity(self) -> int:
        return sum(order.quantity for order in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_qty - self.allocated_quantity

    def can_allocate(self, order: OrderedLine) -> bool:
        return order.quantity <= self.available_quantity and order.sku == self.sku

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta



