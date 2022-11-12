# practice implementation
from transformers import pipeline

generator = pipeline("text-generation")
print(generator("I think", max_length=100))
