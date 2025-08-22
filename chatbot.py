from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
from uuid import uuid4


class Chatbot:
    def __init__(self):
        # Unique session ID for the conversation
        self.session_id = str(uuid4())

        # LLM with streaming support
        self.llm = ChatOllama(model="mistral", stream=True)

        # Prompt template with history support
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        # Build basic chain
        base_chain = self.prompt | self.llm

        # In-memory message history store
        self.memory_store = {}

        # History getter function for RunnableWithMessageHistory
        def get_message_history(session_id: str) -> ChatMessageHistory:
            if session_id not in self.memory_store:
                self.memory_store[session_id] = ChatMessageHistory()
            return self.memory_store[session_id]

        # Wrap the chain with memory capability
        self.chain = RunnableWithMessageHistory(
            base_chain,
            get_message_history,
            input_messages_key="input",
            history_messages_key="history"
        )

    def chat(self):
        print("🤖 Hello! Ask me anything. Type 'exit' to quit.\n")

        while True:
            user_input = input("🧑 You: ")
            if user_input.lower() in {"exit", "quit"}:
                print("👋 Goodbye!")
                break

            # Stream response
            print("🤖 Bot: ", end="", flush=True)
            stream = self.chain.stream(
                {"input": user_input},
                config={"configurable": {"session_id": self.session_id}}
            )

            final_response = ""
            for chunk in stream:
                print(chunk.content, end="", flush=True)
                final_response += chunk.content
            print()


if __name__ == "__main__":
    bot = Chatbot()
    bot.chat()
