import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb import HttpClient # Import the client
import google.generativeai as genai
from app.core.config import settings
from app.services.vector.factory import get_vector_store
import argparse
from app.core.logger import logger

class PrepareData:
    def __init__(self):
        self.vector_store = get_vector_store()
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )

    def ingest_pdf(self,pdf_path:str):
        logger.info(f"🔄 Ingesting: {pdf_path}")

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(pdf_path)

        # Delete existing documents for this source if any
        self.vector_store.delete_by_source(pdf_path)

        loader = PyPDFLoader(pdf_path)
        pages = loader.load()

        chunks = self.splitter.split_documents(pages)

        batch_size = 20

        for i in range(0, len(chunks), batch_size):
            self.vector_store.add_documents(
                chunks[i : i + batch_size]
            )

        logger.info("✅ Ingestion complete")

    def inspect_data(self):
        logger.info("🔍 Inspecting Vector Database Collections...")
        client = HttpClient(host="vector_db", port=8000)
        genai.configure(api_key=settings.LLM_API_KEY)

        models = genai.list_models()
        logger.info(f"Models: {[m.name for m in models]}")
        logger.info(f"Collections: {client.list_collections()}")
        # client.delete_collection(settings.VECTOR_COLLECTION)

def main():
    parser = argparse.ArgumentParser(description="Vector DB ingestion")
    parser.add_argument(
        "--pdf",
        required=True,
        help="Path to PDF file"
    )

    args = parser.parse_args()

    PrepareData().ingest_pdf(args.pdf)
    # PrepareData().inspect_data()


if __name__ == "__main__":
    main()