"""アプリケーション設定"""
import os
from dotenv import load_dotenv

load_dotenv()

# アバター設定
AVATAR_NAME = os.getenv('AVATAR_NAME', 'Spectra')  # AIアシスタント名
AVATAR_FULL_NAME = os.getenv('AVATAR_FULL_NAME', 'Spectra Communicator')  # フルネーム
# AI設定
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']  # 必須：Gemini APIキー（.envファイルに設定）
MODEL_NAME = os.environ['MODEL_NAME']  # 必須：使用モデル名（.envファイルに設定）
SYSTEM_INSTRUCTION = os.getenv('SYSTEM_INSTRUCTION',  # AIの性格・応答スタイル
    f'あなたは{AVATAR_NAME}というAIアシスタントです。技術的で直接的なスタイルで簡潔に応答してください。回答は短く要点を押さえたものにしてください。')

# サーバー設定
SERVER_PORT = int(os.getenv('SERVER_PORT', '5000'))  # ポート
DEBUG_MODE = os.getenv('DEBUG_MODE', 'True').lower() == 'true'  # 開発モード

# UI設定
TYPEWRITER_DELAY_MS = int(os.getenv('TYPEWRITER_DELAY_MS', '50'))  # 文字表示速度(ms)
MOUTH_ANIMATION_INTERVAL_MS = int(os.getenv('MOUTH_ANIMATION_INTERVAL_MS', '150'))  # 口パク切替間隔(ms)
AVATAR_IMAGE_IDLE = 'idle.png'  # アバター静止時画像
AVATAR_IMAGE_TALK = 'talk.png'  # アバター発話時画像

# サウンド設定
BEEP_FREQUENCY_HZ = int(os.getenv('BEEP_FREQUENCY_HZ', '800'))  # ビープ音周波数(Hz)
BEEP_DURATION_MS = int(os.getenv('BEEP_DURATION_MS', '50'))  # ビープ音長さ(ms)
BEEP_VOLUME = float(os.getenv('BEEP_VOLUME', '0.05'))  # ビープ音量(0-1)
BEEP_VOLUME_END = float(os.getenv('BEEP_VOLUME_END', '0.01'))  # ビープ音終了時音量