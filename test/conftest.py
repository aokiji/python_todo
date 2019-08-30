import sys
import os.path
import inspect
from pytest_factoryboy import register

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))


def register_all_factories():
    import test.factory

    for name, obj in inspect.getmembers(test.factory):
        if name.endswith('Factory'):
            register(obj)

register_all_factories()
