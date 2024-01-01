import openai

# Set your OpenAI GPT API key
openai.api_key = 'fevi15'

def generate_answer(question):
    # Make a call to the OpenAI GPT API
    response = openai.Completion.create(
        engine="text-davinci-002",  # or any other GPT engine
        prompt=question,
        max_tokens=100  # Adjust as needed
    )
    
    # Extract and return the generated answer
    answer = response.choices[0].text.strip()
    return answer

# Example usage
user_question = "What is the capital of France?"
answer = generate_answer(user_question)
print("Answer:", answer)
hi je