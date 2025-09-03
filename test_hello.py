from hello import say_hello, add

def test_say_hello():
    """
    To test that function say_hello returns the expected string
    when we offer a specific name input.
    """
    assert (
        say_hello("Annie")
        == "Hello, Annie, welcome to Data Engineering Systems (IDS 706)!"
    )

def test_add():
    """
    To test that the sum of 2 numbers give a correct output.
    """
    assert add(2, 3) == 5
