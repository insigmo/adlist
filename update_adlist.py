from pathlib import Path

import requests
from urllib3 import disable_warnings

disable_warnings()


file_with_links = Path(__file__).parent / 'resources.txt'
file_with_filters = Path(__file__).parent / 'adblock_list.txt'
result = set()

links = file_with_links.read_text()
for link in links.split('\n'):
    try:
        all_filters = requests.get(link, stream=True, verify=False).text.split('\n')
        filters = set(f for f in all_filters if not f.startswith('#') and not f.startswith('!'))
        result |= filters
    except Exception:
        print(link)


file_with_filters.write_text("\n".join(sorted(result)))
