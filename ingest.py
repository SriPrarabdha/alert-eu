import os
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Function to read the EU AI Act text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to chunk the text
def chunk_text(text, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to ingest text into Chroma DB
def ingest_to_chroma(chunks):
    # Initialize Chroma client with persistent storage
    persist_directory = "./chroma_db"
    client = chromadb.PersistentClient(path=persist_directory)
    
    # Create or get collection
    collection_name = "eu-ai-act"
    try:
        collection = client.get_collection(collection_name)
        print(f"Collection '{collection_name}' already exists. Using existing collection.")
    except:
        collection = client.create_collection(collection_name)
        print(f"Created new collection: '{collection_name}'")
    
    # Add documents to collection
    documents = []
    ids = []
    
    for i, chunk in enumerate(chunks):
        documents.append(chunk)
        ids.append(f"chunk-{i}")
    
    # Add documents in batches to avoid potential size limitations
    batch_size = 100
    for i in range(0, len(documents), batch_size):
        end_idx = min(i + batch_size, len(documents))
        batch_docs = documents[i:end_idx]
        batch_ids = ids[i:end_idx]
        
        collection.add(
            documents=batch_docs,
            ids=batch_ids
        )
        print(f"Added batch {i//batch_size + 1}/{(len(documents) + batch_size - 1)//batch_size}")
    
    print(f"Successfully ingested {len(documents)} chunks into ChromaDB")
    print(f"Data is stored persistently at: {os.path.abspath(persist_directory)}")
    return collection

def main():
    file_path = "eu_ai_act.txt"
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    # Read the text file
    print(f"Reading file: {file_path}")
    text = read_text_file(file_path)
    
    # Chunk the text
    print("Chunking text...")
    chunks = chunk_text(text)
    print(f"Created {len(chunks)} chunks")
    
    # Ingest chunks into Chroma DB
    print("Ingesting chunks into ChromaDB...")
    collection = ingest_to_chroma(chunks)
    
    print("Ingestion complete!")

if __name__ == "__main__":
    main()