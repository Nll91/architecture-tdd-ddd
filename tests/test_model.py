import pytest
from datetime import date
from models.model import Batch, OrderedLine


def test_order_equality():
    first_order = OrderedLine(order_id='1234', sku='chair', quantity=3)
    second_order = OrderedLine(order_id='1234', sku='chair', quantity=3)
    assert first_order == second_order


def test_order_inequality():
    first_order = OrderedLine(order_id='1234', sku='chair', quantity=3)
    second_order = OrderedLine(order_id='124', sku='chair', quantity=3)
    assert first_order != second_order


def get_batch_and_order_line(sku, batch_qty, line_qty):
    return (
        Batch(reference='Batch-001', sku=sku, qty=batch_qty, eta=date.today()),
        OrderedLine(order_id='1234', sku=sku, quantity=line_qty)
    )


def test_order_line_can_be_allocated():
    batch_obj, order_obj = get_batch_and_order_line('123', 10, 2)
    batch_obj.allocate(order_obj)
    expected_quantity = 8
    assert batch_obj.available_quantity == expected_quantity


def test_out_of_stock_case():
    batch_obj, order_obj = get_batch_and_order_line('123', 10, 20)
    assert batch_obj.can_allocate(order_obj) is False


def test_sku_equality():
    order_obj = OrderedLine(order_id='1234', sku='chair', quantity=3)
    batch_obj = Batch(reference='Batch-001', sku='table', qty=3, eta=date.today())
    assert batch_obj.can_allocate(order_obj) is False


def test_batch_equality():
    batch1 = Batch(reference='Batch-001', sku='table', qty=3, eta=date.today())
    batch2 = Batch(reference='Batch-001', sku='chair', qty=3, eta=date.today())
    assert batch1 == batch2

def test_batch_inequality():
    batch1 = Batch(reference='Batch-001', sku='table', qty=3, eta=date.today())
    batch2 = Batch(reference='Batch-002', sku='chair', qty=3, eta=date.today())
    assert batch1 != batch2

