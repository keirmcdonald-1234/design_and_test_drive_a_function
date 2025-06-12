from lib.to_do_list import *


def test_includes_hash_to_do():
    assert to_do_finder("#TODO buy milk") == True

def test_does_include_hash_to_do():
    assert to_do_finder("buy milk") == False

def test_contains_to_do_with_no_hash():
    assert to_do_finder("TODO buy crisps") == False