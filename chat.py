import openai

prompt = "You are a chat assistant tasked with helping a user with anything they require."

messages = [{"role": "system", "content": prompt}]

def chat(message):
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response_message = ""
    for choice in response.choices:
        response_message += choice.message.content
    messages.append({"role": "assistant", "content": response_message})
    return response_message
