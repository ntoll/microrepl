import pytest
import io
from unittest.mock import patch
import os
import tempfile

from microrepl import connect_miniterm

@pytest.yield_fixture
def fake_stderr():
    fake_stderr = io.StringIO()
    with patch('sys.stderr', fake_stderr):
        yield fake_stderr

@pytest.yield_fixture
def fake_sys_exit():
    with patch('sys.exit', autospec=True) as fake_exit:
        yield fake_exit


def test_connect_miniterm_suggests_solution_to_perms_problem_on_linux(fake_stderr, fake_sys_exit):
    nonaccessible_port = tempfile.NamedTemporaryFile()
    os.chmod(nonaccessible_port.name, 0o000)
    connect_miniterm(nonaccessible_port.name)
    error_message = fake_stderr.getvalue()
    assert "Found micro:bit, but could not connect." in error_message
    assert "[Errno 13] could not open port" in error_message
    assert "Permission denied: {port!r}".format(port=nonaccessible_port.name) in error_message
    assert 'On linux, try adding yourself to the "dialout" group' in error_message
    assert 'sudo usermod -a -G dialout <your-username>' in error_message
