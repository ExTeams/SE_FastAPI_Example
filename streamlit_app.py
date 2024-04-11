import streamlit as st
from transformers import pipeline
from pydantic import BaseModel
from translate import Translator

class Item(BaseModel):
    text: str

# Инициализация модели
classifier = pipeline("sentiment-analysis")

# Определение функции предсказания
def predict(item: Item):
    return classifier(item.text)

# Основное веб-приложение Streamlit
def main():
    st.title('Анализ тональности')

    # Поле ввода текста
    text_to_translate = st.text_area("Введите текст:", "")
    
    # Создаем объект переводчика
    translator = Translator(from_lang="ru", to_lang="en")

    # Выполняем перевод
    text_input = translator.translate(text_to_translate)
    print(text_input)

    # Кнопка для запуска предсказания
    if st.button("Предсказать"):
        item = Item(text=text_input)
        result = predict(item)
        
        # Отображение результата
        st.write("Тональность:", result[0]['label'])
        st.write("Оценка уверенности:", result[0]['score'])
        

if __name__ == "__main__":
    main()
