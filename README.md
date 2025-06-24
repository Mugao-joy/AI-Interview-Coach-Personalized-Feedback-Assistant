# 🤖 AI Interview Coach — Personalized Interview Feedback Generator

This project builds a smart AI coach that simulates interviews and gives constructive feedback based on how tech companies like Google, Amazon, and Meta would evaluate answers.

---

##  Key Features

- Supports **Zero-Shot**, **Few-Shot**, and **Fine-Tuned** response modes
- Controls tone and creativity using `temperature`, `frequency_penalty`, and `presence_penalty`
- Uploads training data for **OpenAI fine-tuning**
- Includes evaluation metrics to compare modes

- fine tuning should be used as a last resort - work on prompt design,adjust settings eg temperature,use few shot approach,fine tune if all this doesn't give you the results you want
-upload training data(console log to get job ID) after this you can comment it out
-use fileID to create job
-check status of the job
-test the finetuned model
=== you need an effective testing strategy,quality and amount of data is key,its more about the detail not huge changes
---

##  Concepts Covered

| Concept                 | Implemented ✅ |
|-------------------------|----------------|
| Zero-shot prompting     | ✅              |
| Few-shot prompting      | ✅              |
| Prompt tuning           | ✅              |
| Frequency & presence penalties | ✅       |
| Fine-tuning GPT-3.5     | ✅              |
| Testing strategies      | ✅              |

---

## File Descriptions

- `app.py`: Core logic for question → response → feedback
- `prompt_utils.py`: Manages different prompt styles (zero, few-shot)
- `finetune_script.py`: Scripts to upload, create, monitor and test fine-tunes
- `evaluation.py`: Evaluate consistency, tone matching, and cost
- `fine_tune_dataset.jsonl`: 50 examples for training the assistant

---

##  How to Run

### 1. Install dependencies
```bash
pip install openai python-dotenv

---


## Lessons Learned & Troubleshooting Notes

###  Challenge 1: Invalid JSONL Format

**Issue:**  
Training data used `{"prompt": "...", "completion": "..."}`, which is **invalid** for `gpt-3.5-turbo`.

**Fix:**  
Converted dataset to:
```json
{
  "messages": [
    {"role": "user", "content": "Q: ..."},
    {"role": "assistant", "content": "Feedback: ..."}
  ]
}
```

🔗 [OpenAI Fine-Tuning Docs](https://platform.openai.com/docs/guides/fine-tuning)

---

### Challenge 2: Deprecated API Usage

**Issue:**  
Old method `openai.Completion.create(...)` failed in OpenAI SDK `v1+`.

**Fix:**  
Migrated to new API using:

```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client.chat.completions.create(...)
```

🔗 [OpenAI Python SDK on GitHub](https://github.com/openai/openai-python)

---

### ❌ Challenge 3: CLI Tool `prepare_data` Removed

**Issue:**  
`openai tools fine_tunes.prepare_data` no longer works in SDK `v1.x`.

**Fix:**  
Used a Python script to convert legacy `prompt`/`completion` format into `messages` array format.

---

## ✅ Best Practices Applied

- Used prompt engineering, penalties, temperature tuning before fine-tuning
- Only fine-tuned after zero/few-shot prompting couldn't meet tone/format
- Used 50 structured examples for consistent feedback tone
- Tested fine-tuned model with standard and edge-case prompts

---

## 📎 References

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Chat Completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api)
- [OpenAI Fine-Tuning Guide](https://platform.openai.com/docs/guides/fine-tuning)

---