import openai
import requests
from bs4 import BeautifulSoup
import re

# Set up the OpenAI API client
openai.api_key = ""

# Define a function to generate a summary of a Medium article
def generate_summary(url):
    # Use requests and BeautifulSoup to retrieve and parse the article
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the text content of the article
    article = soup.find("article")
    if article is None:
        return "Unable to find article content."

    text = ""
    for p in article.find_all("p"):
        text += p.get_text() + "\n"

    # Remove URLs and other unwanted text using regular expressions
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"Click here to see original article", "", text)
    text = re.sub(r"Get your", "", text)

    # Use the OpenAI API to generate a summary of the text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=280,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Call the function to generate a summary of a Medium article
url = "https://medium.com/@pravse/the-maze-is-in-the-mouse-980c57cfd61a"
summary = generate_summary(url)

# Print the summary
print(summary)
