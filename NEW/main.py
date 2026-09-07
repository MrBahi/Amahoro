import os
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads variables

api_key = os.getenv("OPENAI_API_KEY")

print(api_key)  # prints the key value at runtime


# Returns the value, or None if not found
key = os.getenv("OPENAI_API_KEY")

# Returns the value, or a default string if not found
key = os.getenv("OPENAI_API_KEY", "key-not-set")

# Good practice: stop early if the key is missing
if not key:
    raise ValueError("OPENAI_API_KEY is not set in your .env file")