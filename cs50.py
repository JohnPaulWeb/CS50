import os
from google import genai

# The key comes from an environment variable, never from the file
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("--- Gemini Terminal Chat (Type 'exit' to quit) ---\n")

while True:
    user_prompt = input("You: ")

    if user_prompt.strip().lower() == 'exit':
        print("Goodbye!")
        break

    if not user_prompt.strip():
        continue

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=user_prompt
        )
        print(f"\nGemini: {response.text}\n")

    except Exception as e:
        print(f"\nAn error occurred: {e}\n")