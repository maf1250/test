import openai

client = openai.OpenAI(
    api_key = "sk-poe-LnrqmsQxAB-0U3nFPSXc4DoAtYKmZeHkPapA0Pk696Y",  # or os.getenv("POE_API_KEY")
    base_url = "https://api.poe.com/v1",
)

chat = client.chat.completions.create(
    model = "rayatai",
    messages = [{
      "role": "user",
      "content": "Hello world"
    }]
)

print(chat.choices[0].message.content)
