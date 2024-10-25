import os

import requests
from dotenv import load_dotenv

load_dotenv()


def is_odd(number) -> bool:
    try:
        url = "https://api.openai.com/v1/chat/completions"

        # Construct the request payload
        requestData = {
            "model": "gpt-4o-mini",
            "response_format": {
                "type": "text"
            },
            "messages": [
                {
                    "role": "system",
                    "content": "Answer if number is odd or even. Answer only one word: 'odd' or 'even' or 'unable' in case can not resolve."
                },
                {
                    "role": "user",
                    "content": f"Is {number} odd or even?"
                }
            ],
            "temperature": 1
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
        }

        # Make the POST request to OpenAI API
        response = requests.post(url, json=requestData, headers=headers)
        response.raise_for_status()

        # Parse the response
        choices = response.json().get("choices", [])
        if choices:
            answer = choices[0]["message"]["content"].strip().lower()
            if "odd" in answer:
                return True
            elif "even" in answer:
                return False
            else:
                raise ValueError("Unable to determine if number is odd or even.")
        else:
            raise ValueError("No valid response from OpenAI API.")

    except Exception as e:
        print(f"Error querying OpenAI: {e}")
        raise

