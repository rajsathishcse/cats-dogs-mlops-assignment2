import io
from fastapi.testclient import TestClient
from app import app
from PIL import Image

client = TestClient(app)

def test_predict_valid():
    # Create a dummy image in memory
    img = Image.new('RGB', (224, 224), color = 'white')
    buf = io.BytesIO()
    img.save(buf, format='JPEG')
    buf.seek(0)
    response = client.post("/predict", files={"file": ("test.jpg", buf, "image/jpeg")})
    assert response.status_code == 200
    data = response.json()
    assert "probability" in data
    assert "label" in data

def test_predict_invalid():
    # Send non-image data
    response = client.post("/predict", files={"file": ("test.txt", io.BytesIO(b"not an image"), "text/plain")})
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
