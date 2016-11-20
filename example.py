from googlefinance import getQuotes
from googlefinance import getNews

import json
print(json.dumps(getQuotes('DISHTV'), indent=2))
print(json.dumps(getQuotes('500209'), indent=2))
print(json.dumps(getNews("INFY"), indent=2))