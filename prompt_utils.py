def build_zero_shot_prompt(question, answer):
    return f"Q: {question}\nA: {answer}\nFeedback:"

def build_few_shot_prompt(question, answer):
    few_shot_examples = '''
Q: Tell me about yourself
A: I am a software developer with 3 years of experience.
Feedback: Good answer. Add measurable achievements.

Q: What is your greatest strength?
A: My greatest strength is problem-solving under pressure.
Feedback: Clear strength. Give an example to support it.
'''
    return few_shot_examples + f"\nQ: {question}\nA: {answer}\nFeedback:"
