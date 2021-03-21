from example.hello.say_hello import hello

def test_hello_function_should_return_hello() -> None:
    assert hello() == "hello!"
