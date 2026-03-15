import os
import uuid
import requests
from dotenv import load_dotenv
from auth_util import gen_sign_headers
from pathlib import Path
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
URL = 'https://api-ai.vivo.com.cn/vivogpt/completions'
METHOD = 'POST'
URI = '/vivogpt/completions'
def ask_vivo(prompt):
    request_id = str(uuid.uuid4())
    session_id = str(uuid.uuid4())
    params = {
        'requestId': request_id
    }
    data = {
        'prompt': prompt,
        'model': 'vivo-BlueLM-TB-Pro',
        'sessionId': session_id,
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'
    response = requests.post(URL, json=data, headers=headers, params=params)
    if response.status_code == 200:
        result = response.json()
        if result.get('code') == 0:
            answer = result['data']['content']
            return answer
        else:
            return f"API 错误: {result.get('msg')}"
    else:
        return f"HTTP 错误: {response.status_code}"