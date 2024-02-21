from google.oauth2 import service_account
import google.auth.transport.requests

def get_access_token(service_account_json_path):
    """
    Retrieve a valid access token that can be used to authorize requests.

    :param service_account_json_path: Path to the service account JSON key file.
    :return: Access token or None if retrieval fails.
    """
    SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']

    try:
        # Load credentials from the service account JSON key file
        credentials = service_account.Credentials.from_service_account_file(
            service_account_json_path, scopes=SCOPES)

        # Create a request object
        request = google.auth.transport.requests.Request()

        # Refresh the credentials to obtain a new access token
        credentials.refresh(request)

        # Print the access token
        access_token = credentials.token
        print("Access Token:", access_token)

        return access_token

    except FileNotFoundError:
        print("Error: Service account JSON key file not found at", service_account_json_path)
    except Exception as e:
        print("Error occurred while retrieving access token:", e)

    return None

# Example usage:
access_token = get_access_token('/Users/markjaysonlomboy/Documents/dev-shippingcart-d8be21b2e6c2.json')
if access_token:
    print("Successfully retrieved access token:", access_token)
else:
    print("Failed to retrieve access token.")
