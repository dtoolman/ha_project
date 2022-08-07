import requests
import pandas as pd
from io import StringIO

# TODO: Probably use Mrs. Pavett's login for the header
headers = {
    'Host': 'api.membershipworks.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 
    'Referer': 'https://membershipworks.com/',
    'Cookie': '_gcl_au=1.1.1888969696.1659751184; _ga=GA1.2.1198389599.1659751184; _ga_310VR8R9KJ=GS1.1.1659751184.1.1.1659752050.0',
    'Connection': 'keep-alive',
}
url = 'https://api.membershipworks.com/v1/csv?SF=Ueyb_StsMOohdDJ8tMtlnpY1qp5zjaAoRsETP-fPZg63EvdT52YtG4x-sJel9dRO&_rt=946706400&frm=618575991ea12250a05d87dd'

req = requests.get(url, headers=headers)
data = StringIO(req.text)

df = pd.read_csv(data)
print(df)
