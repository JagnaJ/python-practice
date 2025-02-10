import argparse
import os
import requests

def count_lines(file_path):
    """Counts the number of lines in the given file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"File '{file_path}' contains {len(lines)} line(s).")
    except FileNotFoundError:
        print("Error: File not found!")

def fetch_data(api_url, output_file):
    """Fetches data from the given API URL and saves it to a file."""
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.text

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Data fetched and saved to '{output_file}'.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

parser = argparse.ArgumentParser(description="File processing script.")
parser.add_argument("action", choices=["count", "fetch"], help="Action to perform (count lines or fetch data).")
parser.add_argument("--file", required=True, help="Path to the file to process.")
parser.add_argument("--url", help="API URL to fetch data from (required for 'fetch').")

args = parser.parse_args()

if args.action == "fetch":
    if not args.url:
        print("Error: --url is required for fetching data.")
    else:
        fetch_data(args.url, args.file)

elif args.action == "count":
    count_lines(args.file)