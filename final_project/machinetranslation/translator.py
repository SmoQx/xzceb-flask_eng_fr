"""It's a module whiche has 2 functions to translate from english to french and the other way"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """Translates english text to french"""
    french_text = MyMemoryTranslator(source='en-GB', target='fr-CA').translate(english_text)
    return french_text


def french_to_english(french_text):
    """Translates french text to english"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text


if __name__ == "__main__":
    print(english_to_french("Hello"))
    print(french_to_english("Bonjour"))
