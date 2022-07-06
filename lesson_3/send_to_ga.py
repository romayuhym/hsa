import requests

API_SECRET = "Kx9msRILQ8O2NOazAMZnPQ"
MEASUREMENT_ID = "G-PEZBXEJ881"
CLIENT_ID = "763990736.1657099560"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
}


def send_to_ga(ratio):
    data = {"client_id": CLIENT_ID, "events": [{"name": "test_action", "params": {"ratio": ratio}}]}
    return requests.post(
        "https://www.google-analytics.com/mp/collect",
        json=data,
        params={"measurement_id": MEASUREMENT_ID, "api_secret": API_SECRET},
        headers=HEADER,
    )


if __name__ == "__main__":
    send_to_ga(321)
