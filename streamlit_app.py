import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from hugchat import hugchat

with st.sidebar:
    st.title('🤗💬 HugChat App')
    st.markdown('''
    ## About
    This app is built using:
    - [Streamlit](https://streamlit.io/)
    - [HugChat](https://github.com/Soulter/hugging-chat-api)
    
    💡 Note: No API key required!
    ''')

# Generate empty lists for generated and past values
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm HugChat, How may I help you?"]
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Location of input/response containers
input_container = st.container()
colored_header(
    label='',
    description='',
    color_name='blue-50')
response_container = st.container()

# User input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

with input_container:
    user_input = get_text()
    
# Response output
def query(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response

with response_container:
    if user_input:
        response = query(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        #for i in range(len(st.session_state['generated'])-1, -1, -1):
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
