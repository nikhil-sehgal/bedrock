import boto3

# Initialize Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def ask_bedrock(prompt: str):
    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        body={
            "prompt": prompt,
            "max_tokens_to_sample": 200
        }
    )
    return response["body"].read().decode()

if __name__ == "__main__":
    user_input = input("Ask Bedrock: ")
    print(ask_bedrock(user_input))
