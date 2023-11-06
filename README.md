# GoogleCloud-GenerativeAI-Streamlit-Demo
Multi-page application demo of Streamlit using Google Cloud Generative AI models. Three chatbots are included in the demo.
1. Text Generation Bot
2. Code Generation Bot
3. Customer Service Bot

## Pre-requisites
1. Activate virtual python environment
``` python -m venv venv ``` 
3. [Install Streamlit in Python Virtual Environment](https://docs.streamlit.io/library/get-started/installation)
4. [Install Google Cloud Vertex AI Python SDK](https://cloud.google.com/vertex-ai/docs/start/install-sdk)
5. Authenticate to Google Cloud - [gcloud auth application-default login](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login)
6. Set Environment Variables
   
| **Environment Variable** | **Description** |
| --- | --- |
| MY_PROJECT | Google Cloud Project ID | 
| MY_REGION | Google Cloud Region | 

## Run Application
`streamlit run Hello.py`

