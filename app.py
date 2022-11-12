# practice implementation
from transformers import pipeline

generator = pipeline("text-generation", "gpt2")
source_text = input("Введите фразу для генерации нового текста: ")
text_length = int(input("Введите длину текста: "))
result_text=generator("I think", max_length=100)
print("Сгенерированный текст: ")
print(result_text[0]['generated_text'])
