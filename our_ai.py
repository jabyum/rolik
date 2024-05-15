from openai import OpenAI

client = OpenAI(api_key="sk-proj-TEZXqc6jYGImhbWfwc78T3BlbkFJUGzbOO5k9vT224SpjD7Y")


def chat_gpt3(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user",
                   "content": f"{prompt}"}],
    )
    return response.choices[0].message.content


def text_to_picture(promt):
    response = client.images.generate(model="dall-e-2", prompt=promt)
    return response.data[0].url


