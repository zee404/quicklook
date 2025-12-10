from langchain_google_genai import ChatGoogleGenerativeAI
# 1. FIX: Import from 'langchain_core' instead of 'langchain'
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.core.config import settings

class GeminiService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.3,
            google_api_key=settings.GOOGLE_API_KEY
        )
        
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
            You are a helpful technical assistant.
            Answer the question based ONLY on the following context.
            If the answer is not in the context, say "I don't have that information."
            
            Context:
            {context}
            
            Question: 
            {question}
            
            Answer:
            """
        )
        
        # 2. FIX: Use LCEL (The modern way to chain)
        # Instead of LLMChain, we use the pipe operator (|)
        # Prompt -> LLM -> String Output
        self.chain = self.prompt | self.llm | StrOutputParser()

    def generate_response(self, context_text: str, question: str) -> str:
        # 3. Invoke the chain directly
        response = self.chain.invoke({"context": context_text, "question": question})
        return response