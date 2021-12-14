import os
import pytest
import random

# Declare test data

FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data'
)

ALL_WEBSITES = [
    os.path.join(FIXTURES_DIR, 'webpage1.html'),
    os.path.join(FIXTURES_DIR, 'webpage2.html'),
    os.path.join(FIXTURES_DIR, 'webpage3.html'),
]

@pytest.fixture(scope="module")
def random_website():
    return random.choice(ALL_WEBSITES)