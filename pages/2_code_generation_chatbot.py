import vertexai
import streamlit as st
from vertexai.preview.language_models import CodeGenerationModel
import os

def code_prompt(prompt) -> str:
    
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 1024
    }
    model = CodeGenerationModel.from_pretrained("code-bison@001")
    response = model.predict(
        prefix = prompt, 
        **parameters
    )
    print(f"Response from Model: {response.text}")
    return response.text

if __name__ == '__main__':

    st.title("Code Generation Bot")

    # Initialize Vertex AI
    my_project = os.environ.get('MY_PROJECT')
    my_region = os.environ.get('MY_REGION')
    vertexai.init(project=my_project, location=my_region)

    # Initialize chat history
    if "code" not in st.session_state:
         st.session_state.code = []

    # Display chat messages from history on app rerun
    for message in st.session_state.code:
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.code.append({"role": "user", "content": prompt})
        
        #Send prompt to LLM
        response = code_prompt(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.code.append({"role": "assistant", "content": response})

    