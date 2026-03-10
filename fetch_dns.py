import urllib.request
import json

API_URL = "https://api.recruitment.shq.nz"
API_KEY = "h523hDtETbkJ3nSJL323hjYLXbCyDaRZ"
CLIENT_ID = "100"

def fetch_json(endpoint):
    url = f"{API_URL}{endpoint}?api_key={API_KEY}"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

def main():
    try:
        # Step 1: Fetch domains for the client
        domains = fetch_json(f"/domains/{CLIENT_ID}")

        # Step 2: Iterate through domains and fetch DNS records for each zone
        for domain in domains:
            domain_name = domain.get('name', 'Unknown')
            print(f"Domain: {domain_name}")
            for zone in domain.get('zones', []):
                zone_name = zone.get('name', 'Unknown')
                zone_uri = zone.get('uri')
                if not zone_uri:
                    continue
                print(f"  Zone: {zone_name}")

                records_data = fetch_json(zone_uri)
                # The API description says it returns a list, but actual response is a dict with 'records' key.
                # We handle both for robustness.
                if isinstance(records_data, list):
                    records = records_data
                elif isinstance(records_data, dict):
                    records = records_data.get('records', [])
                else:
                    records = []

                for record in records:
                    # Printing record details: name, type, content, and TTL
                    print(f"    - {record.get('name')} {record.get('type')} {record.get('content')} (TTL: {record.get('ttl')})")
            print("-" * 40)
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
