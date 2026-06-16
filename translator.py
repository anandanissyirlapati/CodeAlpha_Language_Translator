from googletrans import Translator

translator = Translator()

text = input("Enter text: ")

translated = translator.translate(text, dest='te')

print("Translated Text:")
print(translated.text)