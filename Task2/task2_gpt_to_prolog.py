import os
import openai
import re

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Write a Prolog fact that says Alice is Bob's parent."}
    ]
)
content = response.choices[0].message.content
match = re.search(r"```prolog\n(.*?)```", content, re.DOTALL)
prolog_code = match.group(1).strip() if match else content.strip()
with open("facts.pl", "w") as f:
    f.write(prolog_code)

print("Generated Prolog code:\n", prolog_code)
