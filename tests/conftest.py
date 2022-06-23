import random

import pytest


@pytest.fixture
def set_random_seed():
    """Fixture to fixate a specific random seed, as randomness in tests is not very fun"""
    random.seed(43)
