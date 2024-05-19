import openai
from config.settings import settings

openai.api_key = settings.OPENAI_API_KEY

def optimize_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Please optimize the following question for clarity and specificity."},
            {"role": "user", "content": question}
        ],
        max_tokens=50
    )
    optimized_question = response['choices'][0]['message']['content']
    return optimized_question

def generate_answer(question, context, hits):
    formatted_hits = "\n".join([f"Page {hit['page_number']}: {hit['text']}" for hit in hits])
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. When providing an answer, include the relevant text along with the page number where it was found. Make sure you always put the page number of where you got the answer from."},
            {"role": "user", "content": f"Question: {question}\nContext: {context}\nSources:\n{formatted_hits}"}
        ],
        max_tokens=250
    )
    return response['choices'][0]['message']['content']
