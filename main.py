from psaw import PushshiftAPI
import datetime
import pandas as pd

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

# Dictionary for results
submissions = {
    'Author': [],
    'subreddit': [],
    'Time': [],
    'Score': [],
    'Comment': [],
}
# Append results from query into dictionary
for element in query:
    submissions['Author'].append(element.author)
    submissions['subreddit'].append(element.subreddit)
    submissions['Time'].append(datetime.datetime.fromtimestamp(element.created_utc))
    submissions['Score'].append(element.score)
    submissions['Comment'].append(element.body)

# Create DataFrame
df = pd.DataFrame(submissions)

# Use the next line as a debug point in PyCharm and view "df" as DataFrame
print(df.head())
