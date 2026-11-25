import requests

GBFS_URL = "https://gbfs.citibikenyc.com/gbfs/2.3/gbfs.json"
discovery = requests.get(GBFS_URL, timeout=10).json()

# Convert the list of feed objects into a {name: url} lookup dictionary
# Note: For GBFS v3.0+, use discovery["data"]["feeds"] instead of ["en"]
feed_map = {f["name"]: f["url"] for f in discovery["data"]["en"]["feeds"]}

# Now access any endpoint safely by its standardized name
sys_info_url = feed_map.get("system_information")
station_info_url = feed_map.get("station_information")
status_url = feed_map.get("station_status")

if sys_info_url:
    sys_info = requests.get(sys_info_url, timeout=10).json()
    print("System Name:", sys_info["data"]["name"])

if station_info_url:
    station_info = requests.get(station_info_url, timeout=10).json()
    station0 = station_info['data']['stations'][0]
    print("Test station info: ", station0)

if status_url:
    status_info = requests.get(status_url, timeout=10).json()
    for station in status_info['data']['stations']:
        if(station['station_id'] == station0['station_id']):
            station0_status = station
    import pdb; pdb.set_trace()

    print(station0_status)