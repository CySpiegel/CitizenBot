from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])


def translate(text, selectedLanguage):
    translation = translator.translate(text, dest=selectedLanguage)
    return translation


if __name__=="__main__":
    text = "Hello you"
    language = 'es'

    text = translate(text, language)
    print(text.text)