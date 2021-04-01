from utility.utility import StatusCode as status


def test_health_check_ok(test_client):
    response = test_client.get("/api/health_check")
    assert response.status_code == status.HTTP_200_OK
    assert response.json == {"res": "OK"}
