from psaw import PushshiftAPI
import datetime
from database_init import *

database_preparation()
# Limited to 100 results per query
api = PushshiftAPI(max_results_per_request=100)

# Set start and end search dates
todays_date = int(datetime.datetime.today().timestamp())
delta = datetime.timedelta(days=365)
start_date = int((datetime.datetime.today() - delta).timestamp())

# pushshift.io query in wrapper
# Build search using the parameters here: https://pushshift.io/api-parameters/
# pushshift API Wrapper: https://github.com/dmarx/psaw
query = api.search_comments(subreddit='wallstreetbets', after=start_date, before=todays_date, limit=500, author='DeepFuckingValue')

# Append results from query into dictionary
for element in query:
    database_insert(element.author, element.subreddit, datetime.datetime.fromtimestamp(element.created_utc), element.score, element.body)

conn.commit()
conn.close()