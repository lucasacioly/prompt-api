from prompt_engine.engine import Engine
import requests

URL = 'http://localhost:3003/prompt'
OPENAI_API_KEY = "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"

if __name__ == '__main__':
    
    engine = Engine(openai_api_key = OPENAI_API_KEY)

    images = engine.imagine(1)
    img = images[0]

    payload = {
        'prompt':img.prompt, 
        'image':img.bytstream 
    }

    #post request to url
    post_response = requests.post(URL, json=payload)

    