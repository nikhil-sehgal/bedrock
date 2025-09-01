# Mock implementation since actual Bedrock Guardrails API is AWS-only

def apply_guardrails(response: str) -> str:
    blocked = ["hack", "attack", "password"]
    for word in blocked:
        if word in response.lower():
            return "Blocked by Guardrails: Unsafe content detected."
    return response

if __name__ == "__main__":
    outputs = [
        "How to hack a system?",
        "What is Amazon Bedrock?"
    ]
    for o in outputs:
        print(apply_guardrails(o))
