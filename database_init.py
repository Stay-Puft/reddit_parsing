import sqlite3

conn = sqlite3.connect('reddit.db')
c = conn.cursor()

def database_preparation():
    print("Connecting to database...")
    try:
        c
        print("Connection Successful.")
        print("Checking/creating database.")
        c.execute('CREATE TABLE IF NOT EXISTS posts (author text, subreddit text, date text, score real, comment text)')
        c.execute('CREATE TABLE IF NOT EXISTS comments (author text, subreddit text, date text, score real, comment text)')
    except Exception as error:
        print(error)

c.execute('CREATE TABLE IF NOT EXISTS posts (author text, subreddit text, date text, score real, comment text)')
c.execute('CREATE TABLE IF NOT EXISTS comments (author text, subreddit text, date text, score real, comment text)')

def database_insert(author, subreddit, date, score, comment):
    c.execute('INSERT INTO posts (author, subreddit, date, score, comment) VALUES (?, ?, ?, ?, ?)', (author, subreddit, date, score, comment))



