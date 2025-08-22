# 設定値の一元管理
import os
from dotenv import load_dotenv

load_dotenv()

# サーバー設定
SERVER_PORT = int(os.getenv('SERVER_PORT', '5000'))
DEBUG_MODE = os.getenv('DEBUG_MODE', 'True').lower() == 'true'

# AI設定
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
MODEL_NAME = os.environ['MODEL_NAME']
SYSTEM_INSTRUCTION = os.getenv('SYSTEM_INSTRUCTION', 
    'あなたはSpectraというAIアシスタントです。技術的で直接的なスタイルで簡潔に応答してください。回答は短く要点を押さえたものにしてください。')

# UI設定
TYPEWRITER_DELAY_MS = int(os.getenv('TYPEWRITER_DELAY_MS', '50'))

