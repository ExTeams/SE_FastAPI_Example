### Fast API example project
The app uses trained HuggingFace models to predict text sentiment.

#### Documentation 

##### Instaliation
```pip install "uvicorn[standard]"```

##### Run
```uvicorn main:app --reload```
By default application will be start on localhost:8000 / 127.0.0.1:8000

##### Methods

| route        | method | params                               | return                                              |
|--------------|--------|-----------------------------         |-----------------------------------------------------|
| /predict/    | POST   | @Item:{ text: str} :application/json |{'label': 'POSITIVE' / 'NEGATIVE', 'score': number}  |
| /            | GET    |                                      | text/html                                           |
|/sentiment/{text}       | GET     |    text:string                      | {'label': 'POSITIVE' / 'NEGATIVE', 'score': number} |
|/ner/{text}| GET| text:string|{generated_text: string}[]