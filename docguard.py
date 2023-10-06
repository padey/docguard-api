import argparse
import os
import requests
from requests.exceptions import RequestException
import json

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
            # Parse the JSON response
            json_response = response.json()

            # Print the specified values
            print(f'Verdict: **{json_response.get("Verdict", "N/A")}**')
            print(f'FileName: {json_response.get("FileName", "N/A")}')
            print(f'FileType: {json_response.get("FileType", "N/A")}')
            print(f'FileSha256Hash: {json_response.get("FileSha256Hash", "N/A")}')

            # Save the JSON response to a file with the same name as FileSha256Hash
            filename = f'{hash_value}.json'
            with open(filename, 'w') as json_file:
                json_file.write(json.dumps(json_response, indent=4))

            print(f'Response saved as: {filename}')
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
            'password': password,
            'isPublic': public
        }

        # Send the POST request with form fields and the specified file
        response = requests.post(url, headers=headers, data=data, files={'file': (file_path, open(file_path, 'rb'))})

        if response.status_code == 200:
            # Parse the JSON response
            json_response = response.json()

            # Print the specified values
            print(f'Verdict (in bold): **{json_response.get("Verdict", "N/A")}**')
            print(f'FileName: {json_response.get("FileName", "N/A")}')
            print(f'FileType: {json_response.get("FileType", "N/A")}')
            print(f'FileSha256Hash: {json_response.get("FileSha256Hash", "N/A")}')

            # Save the JSON response to a file with the same name as FileSha256Hash
            hash_value = json_response.get('FileSha256Hash', 'unknown')
            filename = f'{hash_value}.json'
            with open(filename, 'w') as json_file:
                json_file.write(json.dumps(json_response, indent=4))

            print(f'Response saved as: {filename}')
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
