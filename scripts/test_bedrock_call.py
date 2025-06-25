from langchain_community.chat_models import BedrockChat
import boto3

# Create Bedrock client for your region
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

# Use Claude 3.5 Sonnet model ID (released June 2024)
model_id = "anthropic.claude-3.5-sonnet-20240620-v1:0"

# Instantiate the chat model
llm = BedrockChat(
    model_id=model_id,
    client=bedrock_runtime,
    model_kwargs={"temperature": 0.2}
)

# Ask your question
question = "What does Medicare cover for cataract surgery?"
response = llm.invoke(question)

print("💬 Claude 3.5 Response:", response)
