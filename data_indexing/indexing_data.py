import llama
from llama import Document, GPTSimpleVectorIndex, SimpleDirectoryReader

# Load JSON objects with content
json_objects = [
    # Load your JSON objects here
]

# Create documents for indexing
documents = [Document(json_obj["content"]) for json_obj in json_objects]

# Create an index with appropriate configuration
index = GPTSimpleVectorIndex.from_documents(
    documents,
    service_context=llama.ServiceContext(
        model_name="text-davinci-003",  # or your preferred LLM
        openai_api_key="YOUR_API_KEY"  # Replace with your OpenAI API key
    )
)

# Save the index for later use (optional)
index.save_to_path("index.llama")

# Function to retrieve closest JSON object during runtime
def retrieve_closest_json(query):
    retrieved_documents = index.retrieve(query)
    closest_doc = retrieved_documents[0]  # Assuming you want the top-ranked result
    return [json_obj for json_obj in json_objects if json_obj["content"] == closest_doc.text][0]

# Example usage:
query = "What are the benefits of using Llama Index?"
closest_json = retrieve_closest_json(query)
print(closest_json)
