import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Upload fine-tuning file
def upload_file(file_path):
    file = client.files.create(file=open(file_path, "rb"), purpose="fine-tune")
    print("File uploaded successfully.")
    print("File ID:", file.id)
    return file.id

# Create fine-tuning job
def create_finetune_job(file_id):
    job = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo"  # Note: GPT-4 is not available for fine-tuning yet
    )
    print("Fine-tune job created.")
    print("Job ID:", job.id)
    return job.id

# Check status of a fine-tuning job
def get_job_status(job_id):
    job_status = client.fine_tuning.jobs.retrieve(job_id)
    print("Job Status:", job_status.status)
    return job_status

# Use the fine-tuned model to generate feedback
def test_fine_tuned_model(model_name, question, answer):
    prompt = f"Q: {question}\nA: {answer}\nFeedback:"
    messages = [
        {"role": "system", "content": "You are an expert interview coach. Give precise and helpful feedback."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=model_name,  # e.g. 'ft:gpt-3.5-turbo-0125:your-org:custom'
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# Run the pipeline
if __name__ == "__main__":
    # STEP 1: Upload file (comment out once done)
    file_path = "fine_tune_dataset.jsonl"
    file_id = upload_file(file_path)

    # STEP 2: Create fine-tuning job
    job_id = 'ftjob-TXElduynzJ1sbCvJNKVQsqKw'#create_finetune_job(file_id)

    # STEP 3: Monitor job status
    print("\nChecking job status...")
    get_job_status(job_id)

    # STEP 4 (optional): Once fine-tuned model is ready
    # Replace with your real fine-tuned model name
    # model_name = "ft:gpt-3.5-turbo-0125:your-org-name:model-id"
    # response = test_fine_tuned_model(model_name, "Tell me about yourself", "I am Joy")
    # print("\nResponse from fine-tuned model:")
    # print(response)
