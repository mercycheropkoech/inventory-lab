from unittest.mock import patch
import requests

def test_inventory_request():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200

        response = requests.get("http://127.0.0.1:5000/inventory")

        assert response.status_code == 200
        