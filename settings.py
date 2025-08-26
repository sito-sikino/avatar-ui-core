"""
設定管理モジュール - .envファイルから全設定を読み込み
"""

import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

# ===========================================
# 必須設定（環境変数が設定されていない場合はエラー）
# ===========================================

# AIプロバイダー選択
AI_PROVIDER = os.getenv('AI_PROVIDER', 'gemini').lower()  # gemini または openai

# プロバイダー別のAPI設定
if AI_PROVIDER == 'openai':
    # OpenAI API設定
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        raise ValueError('AI_PROVIDER=openai is set but OPENAI_API_KEY is not found')
    MODEL_NAME = os.getenv('OPENAI_MODEL_NAME', 'gpt-4.1-mini')

elif AI_PROVIDER == 'gemini':
    # Gemini API設定
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    if not GEMINI_API_KEY:
        raise ValueError('AI_PROVIDER=gemini is set but GEMINI_API_KEY is not found')
    MODEL_NAME = os.getenv('GEMINI_MODEL_NAME', 'gemini-2.0-flash')

else:
    raise ValueError(
        f'Unsupported AI provider: {AI_PROVIDER}. Please specify gemini or openai.'
    )

# ===========================================
# 任意設定（デフォルト値あり）
# ===========================================

# アバター設定
AVATAR_NAME = os.getenv('AVATAR_NAME', 'Spectra')
AVATAR_FULL_NAME = os.getenv('AVATAR_FULL_NAME', 'Spectra Communicator')
AVATAR_IMAGE_IDLE = os.getenv('AVATAR_IMAGE_IDLE', 'idle.png')
AVATAR_IMAGE_TALK = os.getenv('AVATAR_IMAGE_TALK', 'talk.png')

# AI性格設定（AVATAR_NAMEに依存）
SYSTEM_INSTRUCTION = os.getenv(
    'SYSTEM_INSTRUCTION',
    f'あなたは{AVATAR_NAME}というAIアシスタントです。技術的で直接的なスタイルで簡潔に応答してください。回答は短く要点を押さえたものにしてください。'
)

# サーバー設定
SERVER_PORT = int(os.getenv('SERVER_PORT', '5000'))
DEBUG_MODE = os.getenv('DEBUG_MODE', 'True').lower() == 'true'

# UI設定
TYPEWRITER_DELAY_MS = int(os.getenv('TYPEWRITER_DELAY_MS', '50'))
MOUTH_ANIMATION_INTERVAL_MS = int(os.getenv('MOUTH_ANIMATION_INTERVAL_MS', '150'))

# サウンド設定
BEEP_FREQUENCY_HZ = int(os.getenv('BEEP_FREQUENCY_HZ', '800'))
BEEP_DURATION_MS = int(os.getenv('BEEP_DURATION_MS', '50'))
BEEP_VOLUME = float(os.getenv('BEEP_VOLUME', '0.05'))
BEEP_VOLUME_END = float(os.getenv('BEEP_VOLUME_END', '0.01'))
