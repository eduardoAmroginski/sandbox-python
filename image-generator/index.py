import os
import openai
import wget
from dotenv import load_dotenv

load_dotenv()

def generate_image():
    os.system('cls')
    PROMPT = input('What do you want to see? ')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    print('Please wait, generating image...')
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size='1024x1024'
    )

    image_url = response['data'][0]['url']

    response = wget.download(image_url, f"images_generated\{PROMPT[:10]}-{response['created']}.png")

    print('Image generated!')


def menu():
    os.system('cls')
    print(' ')
    print('-------------------------------')
    print(' ')
    print('[1] Generate Image')
    print('[0] Exit')
    print(' ')
    print('-------------------------------')
    print(' ')


if __name__ == '__main__':
    menu()
    option = int(input('Enter your option: '))
    
    while option != 0:
        match option:
            case 1:
                generate_image()
            case _:
                print('Invalid Option')
        
        menu()
        option = int(input('Enter your option: '))