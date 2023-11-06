import vertexai
import streamlit as st
from vertexai.language_models import ChatModel, InputOutputTextPair
import os

def text_prompt(prompt) -> str:

    chat_model = ChatModel.from_pretrained("chat-bison")
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }

    chat = chat_model.start_chat(
        context="""You are a customer service representative of Cymbal.
    Here is Cymbal policy: How many days do I have to return my purchase?
    We offer free returns and exchanges within 30 days of your delivery, with exceptions as described in our Returns Policy. Certain items are designated as final sale and not eligible for returns or exchanges. All on-sale purchases are final.
    """,
        examples=[
            InputOutputTextPair(
                input_text="""I was in a car accident last month and couldn\'t return the item in the 30 days time window. Can you make an exception for me?""",
                output_text="""I understand that you had an emergency and were unable to return your order within the 30-day window. I would be happy to make an exception for you. Please contact our customer service department at 1-555-010--2667 and they will be able to assist you with your return.
    Once your return is approved, you will be issued a return label. Please pack the item carefully and ship it back to us. We will process your refund within 3-5 business days of receiving the returned item."""
            ),
            InputOutputTextPair(
                input_text="""I forgot to return the item within 30 days. Can you make an exception for me?""",
                output_text="""I understand that you want to return the item, but we are unable to return your order since you have missed the 30-day window. Please let me know anything else I can assist you with."""
            )
        ]
    )
    response = chat.send_message(prompt, **parameters)
    return response.text

if __name__ == '__main__':

    st.title("Customer Service Bot")

    # Initialize Vertex AI
    my_project = os.environ.get('MY_PROJECT')
    my_region = os.environ.get('MY_REGION')
    vertexai.init(project=my_project, location=my_region)

    # Initialize chat history
    if "csr" not in st.session_state:
        st.session_state.csr = []

    # Display chat messages from history on app rerun
    for message in st.session_state.csr:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.csr.append({"role": "user", "content": prompt})
        
        #Send prompt to LLM
        response = text_prompt(prompt)

        #response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.csr.append({"role": "assistant", "content": response})

    