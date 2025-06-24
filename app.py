import os
from openai import OpenAI
from dotenv import load_dotenv
from prompt_utils import build_zero_shot_prompt, build_few_shot_prompt

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_feedback(question, answer, mode="few-shot", temperature=0.7, presence_penalty=0.5, frequency_penalty=0.5):
    if mode == "few-shot":
        prompt = build_few_shot_prompt(question, answer)
    else:
        prompt = build_zero_shot_prompt(question, answer)

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are a professional AI interview coach. Provide helpful, structured feedback."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        max_tokens=150
    )

    return completion.choices[0].message.content.strip()

if __name__ == "__main__":
    print("=== AI Interview Coach ===")
    question = input("Enter Interview Question: ")
    answer = input("Enter Your Answer: ")
    mode = input("Prompt mode (zero-shot / few-shot): ").strip()
    feedback = get_feedback(question, answer, mode)
    print("\n--- Feedback ---")
    print(feedback)
