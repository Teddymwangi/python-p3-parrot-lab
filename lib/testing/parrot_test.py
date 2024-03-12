from lib.parrot import parrot

def test_parrot_default():
    assert parrot() == "Squawk!"

def test_parrot_custom():
    assert parrot("Hello, world!") == "Hello, world!"
