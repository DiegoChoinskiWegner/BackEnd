import streamlit as st
from langchain.chains import RetrievalQA



def get_conversation_chain():
    vectorstore = FAISS.from_texts(conversa, embedding)
    chain = RetrievalQA.from_chain_type(
        llm, chain_type="stuff", vectorstore=vectorstore.as_retriever()
        )
    return chain


st.set_page_config(page_title="Crew AI example")

if reset := st.button("resetar Página"):
    reset_st_page()

profissoes = ["Nutricionista", "Educador Físico", "Psicólogo", "Médico"]

seletor_profissoes = st.selectbox(label="Profissões", options=profissoes)


if seletor_profissoes is not None and "chain" not in st.session_state:
    chain = get_conversation_chain(seletor_profissoes)
    st.session_state.chain = chain

if "pdf_messages" not in st.session_state:
    st.session_state.pdf_messages = []

for message in st.session_state.pdf_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Faça uma pergunta ao seu profissional"):
    st.chat_message("user").markdown(prompt)

    st.session_state.pdf_messages.append({"role": "user", "content": prompt})
    chain = st.session_state.chain
    response = chain.run({"query": prompt})

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.pdf_messages.append({"role": "assistant", "content": response})