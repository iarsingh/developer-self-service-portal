from fastapi.testclient import TestClient
from devportal.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'template': 'python-service', 'env': 'dev'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'template': 'python-service', 'env': 'prod'}).json()
    assert bad["passed"] is False
    assert "env" in bad["failed"]
