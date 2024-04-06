#  pip install  openai

import logging

from openai import OpenAI

logging.basicConfig(filename='computer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

client = OpenAI(
    api_key="type your chatgpt api key here"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    }
]

separator = "-" * 50


def computer(message):
    logging.info(message)

    messages.append(
        {
            "role": "user",
            "content": message
        },
    )

    chat = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )

    reply = chat.choices[0].message
    response = reply.content
    logging.info(response)
    logging.info(separator)

    messages.append(reply)
    return response
