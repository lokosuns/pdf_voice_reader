from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path, language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')
        audio_file = gTTS(text=text, lang=language)
        file_name = Path(file_path)
        audio_file.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!'

    else:
        return 'File not exist!!!'


def main():
    file_path = input('\nEnter the file path: ')
    language_file = input("Choose language (etc 'en' or 'ru): ")
    print(pdf_to_mp3(file_path=file_path, language=language_file))


if __name__ == '__main__':
    main()
