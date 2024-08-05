from dataclasses import dataclass


@dataclass
class OrderedLine:
    id: str
    sku: str


class Batch:
    """
    Model domain
    """
    def __init__(self):
        pass

    def associate(self):
        pass
