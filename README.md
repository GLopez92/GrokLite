# GrokLite
The Multi-API Assistant is a Python app that combines multiple APIs into one interface, simplifying tasks like answering questions, web searches, and social media insights. Perfect for researchers, content creators, and professionals, it boosts productivity with automated solutions for knowledge gathering and trend analysis.

# Multi-API Integration Script

This project demonstrates the integration of various APIs, including OpenAI, Bing, and Twitter, to provide versatile functionality like answering questions, performing web searches, and brainstorming ideas from Twitter. 

## Features

- **Answer Questions:** Leverages OpenAI's GPT model to generate intelligent responses to user questions.
- **Web Search:** Uses the Bing API to fetch relevant search results for a query.
- **Brainstorming from Twitter:** Fetches recent tweets related to a specified topic using the Twitter API.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GLopez92/GrokLite.git
   cd GrokLite
Install dependencies: Make sure you have Python 3.7 or higher and run:

bash
Copy code
pip install -r requirements.txt
Set environment variables: Configure your API keys by adding them to an .env file in the project root:

makefile
Copy code
XAI_API_KEY=your_openai_api_key
BING_API_KEY=your_bing_api_key
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
Usage
Running the Script
Execute the script using:

bash
Copy code
python main.py
Available Functions
Answer Questions:

Calls OpenAI's GPT model to provide intelligent responses.
Example:
python
Copy code
print(answer_question("What is the capital of France?"))
Search the Web:

Fetches web search results using the Bing API.
Example:
python
Copy code
results = search_web("Latest AI trends")
for result in results:
    print(f"{result['name']}: {result['url']}")
Brainstorm from Twitter:

Collects recent tweets about a topic using the Twitter API.
Example:
python
Copy code
tweets = brainstorm_from_twitter("AI innovation")
print(tweets)
Grok Lite Function:

Simplifies interaction with various functionalities.
Example:
python
Copy code
print(grok_lite("question", "What is the capital of France?"))
print(grok_lite("search", "Latest AI trends"))
print(grok_lite("brainstorm", "AI innovation"))
Requirements
Python 3.7 or higher
openai Python library
requests library
tweepy library
Install dependencies with:

bash
Copy code
pip install -r requirements.txt
Notes
Ensure you have valid API keys for OpenAI, Bing, and Twitter.
Use environment variables for security and flexibility.
Error handling is implemented to handle common API issues.
License
This project is licensed under the MIT License.

Author
Guillermo Lopez
GitHub: GLopez92
Project Repository: GrokLite
