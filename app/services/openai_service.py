import openai
from config.settings import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_answer(question, context, hits):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. When providing an answer, include the relevant text along with the page number where it was found. No matter what, always return only 1 page number in the prompt and no more than that"},
            {"role": "user", "content": f"{context}\n\n{question}"}
        ],
        max_tokens=400
    )
    answer = response['choices'][0]['message']['content']
    detailed_answer = answer + "\n\nReferences:\n"
    
    for hit in hits:
        detailed_answer += f"Page {hit['page_number']}: {hit['text'][:100]}...\n"

    return detailed_answer
