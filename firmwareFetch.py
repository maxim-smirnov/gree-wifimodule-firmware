#!/usr/bin/env python

import os
import sys
import json
import requests

def fetch_and_save_data(firmware_code, server):
    # Define the URL
    url = f'http://{server}/wifiModule/Lastversion?firmwareCode={firmware_code}'

    try:
        # Fetch JSON data using requests
        response = requests.get(url,verify=False)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()

        # Check if the response status is 405
        if data.get('r') == 405:
            print(f"Ignore firmware code {firmware_code} from {server} due to response status 405")
            return

        # Prepare filename
        version = data.get('ver')
        filename = f"downloaded/{firmware_code}_v{version}_{server}.md"

        # Write data to MD file
        with open(filename, 'w') as file:
            file.write(f"`{url}`\n\n")
            file.write(f"```json\n")
            json.dump(data, file, indent=2)
            file.write(f"\n```")

        print(f"Data saved for firmware code {firmware_code} from {server}")
        return firmware_code, filename, data

    except requests.RequestException as e:
        print(f"Error fetching data for firmware code {firmware_code} from {server}: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response for firmware code {firmware_code} from {server}: {str(e)}")


def fetch_firmware(firmware_code, filename, data):
    print(f'Downloading {firmware_code} from {data["url"]}')
    resp = requests.get(data['url'])
    fname = resp.headers['Content-Disposition'].replace('attachment; filename="', "")[:-1]
    tmp_bin = os.path.join("downloaded", fname)
    with open(tmp_bin, 'wb') as f:
        print(f'Recieved {fname}')
        f.write(resp.content)

    print(f"Wrote {tmp_bin}")
    target_bin = os.path.join(firmware_code, fname)
    if os.path.exists(target_bin):
        print(f'File {target_bin} already exists - skipping')
        return

    print(f'Renaming {tmp_bin} to {target_bin}')
    os.rename(tmp_bin, target_bin)
    print(f'Renaming {filename} to {target_bin.replace(".bin", ".md")}')
    os.rename(filename, target_bin.replace(".bin", ".md"))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <firmware_code>")
        sys.exit(1)

    firmware_code = sys.argv[1]
    servers = [
        "grih.gree.com",
        "tmp.grih.gree.com",
        "kfgrih.gree.com",
        "test.grih.gree.com",
        "ru.grih.gree.com",
        "na.grih.gree.com",
        "hk.grih.gree.com",
        "eu.grih.gree.com",
        "in.grih.gree.com",
        "sa.grih.gree.com"
    ]

    # Create the "downloaded" directory if it doesn't exist
    os.makedirs("downloaded", exist_ok=True)

    for server in servers:
        res = fetch_and_save_data(firmware_code, server)
        if res: fetch_firmware(*res)
