# Import library
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import PyPD
from langchain_openai import OpenAiEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

# Create a document loader for rag_paper.pdf
loader_pdf = PyPDFLoader('rag_paper.pdf')
# Create a document loader for unstructured HTML
loader_html = UnstructuredHTMLLoader(file_path = 'datacamp-blog.html')

# Load the document
data_pdf= loader_pdf.load()

data_html = loader_html.load()

# Print the document's content
print(data_pdf[0])

# Print the first document's content
print(data_html[0].page_content)

# Print the first document's metadata
print(data_html[0].metadata)


# Divide the text in chunks
text = "deuhduesuhd  nidunq dd mpij oiwe /n/n"

text_splitter = CharacterTextSplitter(
    separator="/n/n",
    chunk_size= 100,
    chunk_overlap= 10
)

chunks= text_splitter.split_text(text)

print(chunks)

# Splt the document in chunks
splitter = RecursiveCharacterTextSplitter(chuck_size=1000, chunk_overlap=200)

chuncks_doc = splitter.split_documents(data_pdf)

print(chuncks_doc)

# Embedding and Storing chunks

embedding_model = OpenAIEmbeddings(
    api_key=openai_api_key,
    model="text-embedding-3-small"
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)


prompt = ChatPromptTemplate.from_template("""
    Use the following pieces ofcontext to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Context: {context}
    Question: {question}
""")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0)


chain = (
    {"context": retriever, "question": HumanMessagePromptTemplate(prompt)}
    | prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke({"question": "What are the key findings or results presented in the paper?"})


