# Firebase Messaging Access Token Retrieval

This script retrieves a valid access token that can be used to authorize requests for Firebase Cloud Messaging.

## Prerequisites

Before running the script, ensure you have:

- Python installed on your system.
- Service account JSON key file with appropriate permissions for Firebase Cloud Messaging.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install google-auth

RUN
python3 getToken.py

NEW FIREBASE PUSH NOTIFICATION ENDPOINT
https://fcm.googleapis.com/v1/projects/dev-shippingcart/messages:send

SAMPLE PAYLOAD
{
    "message": {
        "token":"FCM_ TOKEN",
        "notification": {
            "title": "TEST",
            "body": "TEST",
            "image": "IMAGE"
        },
        "data": {
            "key1": "value1",
            "key2": "value2"
        }
    }
}
