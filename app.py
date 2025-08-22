"""Webアプリケーション"""
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import settings

# Gemini API接続
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name=settings.MODEL_NAME,
    system_instruction=settings.SYSTEM_INSTRUCTION
)
chat = model.start_chat()  # チャットセッション開始

app = Flask(__name__)

@app.route('/')
def index():
    """メインページ表示"""
    config = {
        'typewriter_delay': settings.TYPEWRITER_DELAY_MS,
        'avatar_name': settings.AVATAR_NAME,
        'avatar_full_name': settings.AVATAR_FULL_NAME,
        'mouth_animation_interval': settings.MOUTH_ANIMATION_INTERVAL_MS,
        'beep_frequency': settings.BEEP_FREQUENCY_HZ,
        'beep_duration': settings.BEEP_DURATION_MS,
        'beep_volume': settings.BEEP_VOLUME,
        'beep_volume_end': settings.BEEP_VOLUME_END,
        'avatar_image_idle': settings.AVATAR_IMAGE_IDLE,
        'avatar_image_talk': settings.AVATAR_IMAGE_TALK
    }
    return render_template('index.html', config=config)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """ユーザー入力を受信しAI応答を返す"""
    message = request.json['message']
    response = chat.send_message(message)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=settings.DEBUG_MODE, port=settings.SERVER_PORT)