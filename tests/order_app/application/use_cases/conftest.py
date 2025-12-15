from unittest.mock import MagicMock

import pytest


@pytest.fixture
def order_repository():
    class MockOrderRepository:
        def __init__(self):
            self.save = MagicMock()
            self.delete = MagicMock()
            self.get_by_id = MagicMock()
            self.get_list = MagicMock()

    return MockOrderRepository()
