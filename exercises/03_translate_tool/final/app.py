# conda install -c conda-forge googletrans
# TODO - make this more challenging, turn into a command line application

from googletrans import Translator


def translate(term, **kwargs):
    translator = Translator()
    
    translation = translator.translate(term, **kwargs)

    return translation

if __name__ == '__main__':
    result = translate('buon giorno, principessa!')
    print(f'That looks like "{result.src}"')
    print(result.text)