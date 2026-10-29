import subprocess
import sys


def test_hello_output():
    result = subprocess.run(
        [sys.executable, "hello.py"], capture_output=True, text=True
    )
    assert result.stdout == "Hello from claude-sonnet-5\n"
