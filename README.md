# 🤖 AI Interview Coach — Personalized Interview Feedback Generator

This project builds a smart AI coach that simulates interviews and gives constructive feedback based on how tech companies like Google, Amazon, and Meta would evaluate answers.

---

##  Key Features

- Supports **Zero-Shot**, **Few-Shot**, and **Fine-Tuned** response modes
- Controls tone and creativity using `temperature`, `frequency_penalty`, and `presence_penalty`
- Uploads training data for **OpenAI fine-tuning**
- Includes evaluation metrics to compare modes

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

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install openai python-dotenv
