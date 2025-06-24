def evaluate_responses(results):
    for mode, response in results.items():
        print(f"\nMode: {mode}")
        print("Feedback:", response)
        print("Length:", len(response.split()))
        print("Contains actionable advice:", "Yes" if any(x in response.lower() for x in ["add", "improve", "more", "specific", "example"]) else "No")
