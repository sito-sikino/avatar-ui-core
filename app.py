"""Webアプリケーション"""

from flask import Flask, render_template, request, jsonify
import settings
import traceback

# AI APIの初期化
chat_session = None
previous_response_id = None  # OpenAI Responses API用の前回のレスポンスID

if settings.AI_PROVIDER == 'openai':
    # OpenAI API初期化
    from openai import OpenAI

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

elif settings.AI_PROVIDER == 'gemini':
    # Gemini API初期化
    import google.generativeai as genai

    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel(
        model_name=settings.MODEL_NAME, system_instruction=settings.SYSTEM_INSTRUCTION
    )
    chat_session = model.start_chat()  # チャットセッション開始

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
        'avatar_image_talk': settings.AVATAR_IMAGE_TALK,
        'ai_provider': settings.AI_PROVIDER,
        'model_name': settings.MODEL_NAME,
    }
    return render_template('index.html', config=config)


@app.route('/api/chat', methods=['POST'])
def api_chat():
    """ユーザー入力を受信しAI応答を返す"""
    try:
        message = request.json['message']

        if settings.AI_PROVIDER == 'openai':
            global previous_response_id

            # OpenAI Responses APIを使用（正式リリース版）
            # 初回のリクエストか、継続のリクエストかで分岐
            if previous_response_id is None:
                # 初回：システムプロンプトとユーザーメッセージを含める
                response = client.responses.create(
                    model=settings.MODEL_NAME,
                    input=[
                        {'role': 'system', 'content': settings.SYSTEM_INSTRUCTION},
                        {'role': 'user', 'content': message},
                    ],
                )
            else:
                # 継続：previous_response_idを使って会話を継続
                response = client.responses.create(
                    model=settings.MODEL_NAME,
                    input=message,
                    previous_response_id=previous_response_id,
                )

            # レスポンスIDを保存
            previous_response_id = response.id

            # Responses APIの output_text プロパティから直接テキストを取得
            ai_response = response.output_text

            return jsonify({'response': ai_response})

        elif settings.AI_PROVIDER == 'gemini':
            # Gemini APIを使用
            response = chat_session.send_message(message)
            return jsonify({'response': response.text})

    except Exception as e:
        # エラーハンドリング
        error_message = f'Error occurred: {str(e)}'
        print(f'[ERROR] {error_message}')
        print(traceback.format_exc())

        return (
            jsonify(
                {
                    'error': error_message,
                    'provider': settings.AI_PROVIDER,
                    'model': settings.MODEL_NAME,
                }
            ),
            500,
        )


if __name__ == '__main__':
    print(f'=== Avatar UI Core ===')
    print(f'AI Provider: {settings.AI_PROVIDER}')
    print(f'Model: {settings.MODEL_NAME}')
    print(f'Server running at: http://localhost:{settings.SERVER_PORT}')
    print(f'====================')

    app.run(debug=settings.DEBUG_MODE, port=settings.SERVER_PORT)
