from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
import sys

class LLM:
	def __init__(self, msg):
		# Template
		template = "you are AI Bot, name Dora, answer to prompt : {req}."
		prompt = PromptTemplate.from_template(template)

		# Model and streaming
		llm = ChatOllama(model="mistral", stream=True)

		# Chain
		chain = prompt | llm

		# Stream the response
		print("🧠 Response:", end=" ", flush=True)
		for chunk in chain.stream({"req": msg}):
			print(chunk.content, end="", flush=True)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python LLM.py <prompt_message>")
	else:
		app = LLM(sys.argv[1])
