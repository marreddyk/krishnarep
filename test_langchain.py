from langchain.prompts import PromptTemplate

template = "What are the Medicare coverage details for {topic}?"
prompt = PromptTemplate.from_template(template)

filled_prompt = prompt.format(topic="cataract surgery")
print("🧠 Prompt Sent to LLM:", filled_prompt)
