import boto3

# Initialize Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def summarize_text(text: str):
    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        body={
            "prompt": f"Summarize this text in 3 sentences:\n\n{text}",
            "max_tokens_to_sample": 200
        }
    )
    return response["body"].read().decode()

if __name__ == "__main__":
    article = """
    Amazon Bedrock provides access to foundation models via API.
    Developers can build chatbots, summarizers, and RAG systems without managing infrastructure.
    It integrates with the AWS ecosystem and supports multiple providers.
    """
    print("Summary:", summarize_text(article))
