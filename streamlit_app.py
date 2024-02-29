import streamlit as st
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

# Инициализация модели
classifier = pipeline("sentiment-analysis")

# Определение функции предсказания
def predict(item: Item):
    return classifier(item.text)

# Основное веб-приложение Streamlit
def main():
    st.title('Sentiment Analysis with Streamlit')

    # Поле ввода текста
    text_input = st.text_area("Enter text:", "")

    # Кнопка для запуска предсказания
    if st.button("Predict"):
        item = Item(text=text_input)
        result = predict(item)
        
        # Отображение результата
        st.write("Sentiment:", result[0]['label'])
        st.write("Confidence Score:", result[0]['score'])

if __name__ == "__main__":
    main()
