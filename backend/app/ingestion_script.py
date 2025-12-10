import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from chromadb import HttpClient # Import the client

def ingest_pdf():
    PDF_PATH = "app/data/aws-overview.pdf"
    print(f"🔄 Starting Remote Ingestion for: {PDF_PATH}")
    
    if not os.path.exists(PDF_PATH):
        # Fallback logic
        local_fallback = f"data/{os.path.basename(PDF_PATH)}"
        if os.path.exists(local_fallback):
             PDF_PATH = local_fallback
        else:
            print("❌ File not found.")
            return

    # 1. LOAD
    print("   - Loading PDF...")
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()
    pages = pages[:50] 
    print(f"   - Loaded {len(pages)} pages.")

    # 2. SPLIT
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(pages)

    # 3. EMBEDDINGS
    print("   - Loading Local Embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 4. CONNECT TO DOCKER DATABASE (The Fix)
    # We connect to the container named "vector_db" on port 8000
    print("   - Connecting to Vector DB Container...")
    client = HttpClient(host="vector_db", port=8000)
    
    vector_db = Chroma(
        client=client,
        collection_name="quicklook_knowledge",
        embedding_function=embeddings,
    )

    # 5. UPLOAD
    batch_size = 20
    print("   - Uploading vectors to database container...")
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        print(f"     Processing batch {i//batch_size + 1}/{(len(chunks)//batch_size)+1}...")
        vector_db.add_documents(batch)
            
    print(f"✅ Success! Data is now stored inside the 'vector_db' container.")

def inspect_data():
    print("🔍 Inspecting Vector Database Collections...")
    client = HttpClient(host="vector_db", port=8000)
    print(client.list_collections())
if __name__ == "__main__":
    inspect_data()