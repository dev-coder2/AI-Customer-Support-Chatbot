import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def query_gpt4(user_query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content": user_query}]
    )
    return response['choices'][0]['message']['content']
