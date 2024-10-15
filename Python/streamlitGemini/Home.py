import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Bem vindo a Demo do Wegner")


st.sidebar.success("Select a demo above.")


st.markdown(
    """
    Está a primeira impressão que quero passar sobre meu conhecimento de alguns Framworks.
    
    **👈 Olhe ao lado ** para encontrar algun exemplos
    ### Quais frameworks estamos falando?
    - Streamlit [streamlit.io](https://streamlit.io)
    - Gemini [documentation](https://docs.streamlit.io)
    - Crew AI [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)


st.write('''Curtiu?? Se quiser deixar sua opinião''')
st.checkbox("sim")
st.checkbox("não")