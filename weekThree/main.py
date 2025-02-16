import argparse
from file_manager import FileManager
from api_client import APIClient

def main():
    parser = argparse.ArgumentParser(description="File and API management script.")
    parser.add_argument("action", choices=["count", "fetch"], help="Action to perform (count lines or fetch data).")
    parser.add_argument("--file", required=True, help="Path to the file.")
    parser.add_argument("--url", help="API URL to fetch data from.")
    args = parser.parse_args()

    file_manager = FileManager(args.file)

    if args.action == "fetch":
        if not args.url:
            print("Error: --url is required for fetching data.")
            return
        api_client = APIClient(args.url)
        data = api_client.fetch_data()
        file_manager.write_data(data)
        print("Data fetched and written to the file.")
    elif args.action == "count":
        lines = file_manager.count_lines()
        print(f"File '{args.file}' contains {lines} line(s).")

if __name__ == "__main__":
    main()