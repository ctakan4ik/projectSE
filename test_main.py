from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Translate ru-en app. Use method /translate"}


def test_predict_main1():
    response = client.post('/translate/', data={'assignment': 'Мне нравится машинное обучение'}) 
    assert response.status_code == 200
    assert 'I like machine learning' in response.text

def test_predict_main2():
    response = client.post('/translate/', data={'assignment': 'Ингрия будет свободной'}) 
    assert response.status_code == 200
    assert 'Ingria will be free' in response.text

def test_predict_main3():
    response = client.post('/translate/', data={'assignment': 'Кто проживает на дне океана?'}) 
    assert response.status_code == 200
    assert 'Who lives at the bottom of the ocean?' in response.text