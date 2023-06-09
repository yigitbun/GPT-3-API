import openai
import re

# Set up the OpenAI API client
openai.api_key = ""

# Define a function to generate a summary of a set of tweets
def generate_summary(tweets):
    # Combine the tweets into a single string
    text = " ".join(tweets)

    # Remove URLs and usernames from the text using regular expressions
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)

    # Use the OpenAI API to generate a summary of the text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.9,
    )

    return response.choices[0].text.strip()

# Define a function to read a set of tweets from a file
def read_tweets(filename):
    with open(filename, "r") as file:
        tweets = file.readlines()

    return [tweet.strip() for tweet in tweets]

# Call the functions to read the tweets and generate a summary
tweets = read_tweets("tweets.txt")
summary = generate_summary(tweets)

# Print the summary
print(summary)
