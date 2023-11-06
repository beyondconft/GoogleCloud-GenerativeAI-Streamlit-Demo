# GoogleCloud-GenerativeAI-Streamlit-Demo
Multi-page application demo of Streamlit using Google Cloud Generative AI models. Three chatbots are included in the demo.
1. Text Generation Bot
2. Code Generation Bot
3. Customer Service Bot

## Pre-requisites
1. Activate virtual python environment \
```
python3 -m venv venv
source venv/vin/activate
```
2. [Install Streamlit in Python Virtual Environment](https://docs.streamlit.io/library/get-started/installation) \
   ``` pip install streamlit ```
3. [Install Google Cloud Vertex AI Python SDK](https://cloud.google.com/vertex-ai/docs/start/install-sdk) \
   ``` pip install google-cloud-aiplatform ```
4. Authenticate to Google Cloud - [gcloud auth application-default login](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login) \
   ``` gcloud auth application-default login ```
5. Set Environment Variables \
   ```
   export MY_PROJECT=google-cloud-project-id
   export MY_REGION=google-cloud-region
   ```
   
| **Environment Variable** | **Description** |
| --- | --- |
| MY_PROJECT | Google Cloud Project ID | 
| MY_REGION | Google Cloud Region | 

## Run Application
`streamlit run Hello.py`

