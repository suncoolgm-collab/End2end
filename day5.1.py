import json
from datetime import datetime

a=json.dumps({1, 2, 3})
#TypeError: Object of type set is not JSON serializable

b=json.loads("{'menu': '라떼'}")
#json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

c=json.dumps({"when": datetime.now()})
#TypeError: Object of type datetime is not JSON serializable when serializing dict item 'when'