import argparse
import requests
from requests.exceptions import RequestException
import json
import curlify

def send_get_request(apikey, hash_value):
    # Construct the URL for the GET request with the hash value
    url = f'https://api.docguard.io/api/FileAnalyzing/GetByHash/{hash_value}'

    # Set the headers with the API key
    headers = {
        'x-api-key': apikey
    }

    try:
        # Send the GET request
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parse and format the JSON response
            json_response = response.json()
            formatted_response = json.dumps(json_response, indent=4)  # Format the JSON
            print(formatted_response)

            # Print the executed curl command for debugging
            curl_command = curlify.to_curl(response.request)
            print(f'curl command: {curl_command}')
        else:
            print(f'Error: {response.status_code} - {response.text}')

    except RequestException as e:
        print(f'Error sending the GET request: {e}')

def send_post_request(apikey, file_path, password="infected", public="false"):
    # Construct the URL for the POST request
    url = 'https://api.docguard.io/api/FileAnalyzing/AnalyzeFile/'

    # Set the headers with the API key
    headers = {
        'x-api-key': apikey
    }

    try:
        # Create a dictionary for form fields, including the 'file' parameter
        data = {
            'file': (None, open(file_path, 'rb')),
            'isPublic': public
        }

        # Send the POST request with form fields in the payload
        response = requests.post(url, headers=headers, files=data)

        if response.status_code == 200:
            # Parse and format the JSON response
            json_response = response.json()
            formatted_response = json.dumps(json_response, indent=4)  # Format the JSON
            print(formatted_response)

            # Print the executed curl command for debugging
            curl_command = curlify.to_curl(response.request)
            print(f'curl command: {curl_command}')
        else:
            print(f'Error: {response.status_code} - {response.text}')

    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except RequestException as e:
        print(f'Error sending the POST request: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send GET or POST request to an API.')
    parser.add_argument('-search', action='store_true', help='Perform a hash search')
    parser.add_argument('-submit', action='store_true', help='Submit a file for analysis')
    parser.add_argument('-api-key', required=True, help='API key')
    parser.add_argument('-hash', help='Hash value (for search)')
    parser.add_argument('-file', help='Path to the file to submit (for submit)')
    parser.add_argument('-password', default='infected', help='Password (optional)')
    parser.add_argument('-public', default='false', help='Public (optional, default=false)')

    args = parser.parse_args()

    if args.search:
        if not args.hash:
            print("Error: -hash is required for search.")
        else:
            send_get_request(args.api_key, args.hash)
    elif args.submit:
        if not args.file:
            print("Error: -file is required for submit.")
        else:
            send_post_request(args.api_key, args.file, args.password, args.public)
    else:
        print("Error: You must specify either -search or -submit.")
