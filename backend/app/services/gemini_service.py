from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.core.config import settings

class GeminiService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.3,
            google_api_key=settings.GOOGLE_API_KEY
        )
        
        # Define the personality and instructions
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
            You are a helpful assistant for the QuickLook internal tool.
            Use the following context to answer the user's question.
            If the answer is not in the context, say "I don't have that information in my knowledge base."
            
            Context:
            {context}
            
            Question: 
            {question}
            
            Answer:
            """
        )

    def generate_response(self, context_text: str, question: str) -> str:
        """
        Sends the prompt to Gemini and gets the text string back.
        """
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        response = chain.invoke({"context": context_text, "question": question})
        return response['text']