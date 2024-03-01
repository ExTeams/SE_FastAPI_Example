# FastAPI Sentiment Analysis Service Documentation ##
## Introduction
This FastAPI service provides sentiment analysis using the Hugging Face Transformers library. Sentiment analysis involves determining the sentiment or emotion expressed in a given text, and this service uses a pre-trained sentiment analysis model from the Transformers library.

## Usage
### 1. Installation
To run the service, you need to install the required dependencies. You can install them using the following:

```bash
pip install fastapi transformers uvicorn
```
### 2. Running the Service
Once the dependencies are installed, you can run the FastAPI service with the following command:

```bash
uvicorn main:app --reload
```
### 3. Endpoints
3.1 Root Endpoint
URL: /
Method: GET
Description: Returns a simple message indicating that the FastAPI service has started.
Example
```bash
curl -X 'GET' 'http://127.0.0.1:8000/'
```
Response:

```bash
{"FastApi service started!"}
```
3.2 Sentiment Analysis Endpoint
URL: /{text}
Method: GET
Description: Performs sentiment analysis on the provided text using a pre-trained sentiment analysis model.
Parameters
text (string): The text for sentiment analysis.
Example
```bash
curl -X 'GET' 'http://127.0.0.1:8000/This is a positive text.'
```
Response:

```bash
{"label": "POSITIVE", "score": 0.9998}
```
3.3 Prediction Endpoint
URL: /predict/
Method: POST
Description: Performs sentiment analysis on the text provided in the request body using a pre-trained sentiment analysis model.
### Request Body
item (object): A Pydantic model with a single attribute text representing the text for sentiment analysis.
Example
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "This is a positive text."
}'
```
Response:

```bash
{"label": "POSITIVE", "score": 0.9998}
```
Conclusion
This FastAPI service provides a simple interface for sentiment analysis using the Hugging Face Transformers library. The service exposes endpoints for obtaining sentiment analysis results both through query parameters and POST requests with JSON data.