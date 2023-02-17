
def test_create_stats(client):
    data = {
          "date": "2023-01-15",
          "views": 1000,
          "clicks": 1000,
          "cost": 100
        }
    response = client.post("/stats/", json=data)
    assert response.status_code == 201


def test_create_stats_without_views(client):
    data = {
          "date": "2023-01-15",
          "clicks": 1000,
          "cost": 100
        }
    response = client.post("/stats/", json=data)
    assert response.status_code == 201


def test_failed_stats_without_date(client):
    data = {
          "clicks": 1000,
          "cost": 100
        }
    response = client.post("/stats/", json=data)
    assert response.status_code == 422


def test_show_stats(client):
    data_first = {
          "date": "2023-01-15",
          "views": 101,
          "clicks": 101,
          "cost": 10
        }
    data_second = {
        "date": "2023-02-15",
        "views": 1000,
        "clicks": 1000,
        "cost": 100
    }
    response_first = client.post("/stats/", json=data_first)
    response_second = client.post("/stats/", json=data_second)
    date = {
        "from_date": "2023-02-01",
        "to_date": "2023-02-27"
    }
    resp = client.post("/stats/show_stats", json=date)

    assert response_first.status_code == 201
    assert response_second.status_code == 201
    assert resp.status_code == 200
    assert resp.json()["result"][0]["views"] == 1000


def test_show_stats_without_views(client):
    data_first = {
          "date": "2023-01-15",
          "views": 101,
          "clicks": 101,
          "cost": 10
        }
    data_second = {
        "date": "2023-02-15",
        "clicks": 1000,
        "cost": 100
    }
    response_first = client.post("/stats/", json=data_first)
    response_second = client.post("/stats/", json=data_second)
    date = {
        "from_date": "2023-02-01",
        "to_date": "2023-02-27"
    }
    resp = client.post("/stats/show_stats", json=date)

    assert response_first.status_code == 201
    assert response_second.status_code == 201
    assert resp.status_code == 200
    assert resp.json()["result"][0]["cpm"] == 0


def test_delete_stats(client):
    data_first = {
          "date": "2023-01-15",
          "views": 101,
          "clicks": 101,
          "cost": 10
        }
    data_second = {
        "date": "2023-02-15",
        "clicks": 1000,
        "cost": 100
    }
    response_first = client.post("/stats/", json=data_first)
    response_second = client.post("/stats/", json=data_second)

    resp_del = client.get("/stats/delete_stats")

    date = {
        "from_date": "2023-02-01",
        "to_date": "2023-02-27"
    }
    resp = client.post("/stats/show_stats", json=date)

    assert response_first.status_code == 201
    assert response_second.status_code == 201
    assert resp.status_code == 200
    assert resp.json()["result"] == []




