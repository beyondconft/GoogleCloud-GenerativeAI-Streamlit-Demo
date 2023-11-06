import vertexai
import streamlit as st
from vertexai.language_models import TextGenerationModel
import os

def text_prompt(prompt) -> str:
    
    parameters = {
        "candidate_count": 1,
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        prompt,
        **parameters
    )
    print(f"Response from Model: {response.text}")
    return response.text

if __name__ == '__main__':

    st.title("Text Generation Bot")

    # Initialize Vertex AI
    my_project = os.environ.get('MY_PROJECT')
    my_region = os.environ.get('MY_REGION')
    vertexai.init(project=my_project, location=my_region)

    # Initialize chat history
    if "messages" not in st.session_state:
         st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        #send prompt to LLM
        response = text_prompt(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    