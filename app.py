"""Webアプリケーション"""
from flask import Flask, render_template, request, jsonify
import settings
import traceback

# AI APIの初期化
chat_session = None

if settings.AI_PROVIDER == 'openai':
    # OpenAI API初期化
    from openai import OpenAI
    
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    # チャット履歴を保持
    messages = [
        {"role": "system", "content": settings.SYSTEM_INSTRUCTION}
    ]
    
elif settings.AI_PROVIDER == 'gemini':
    # Gemini API初期化
    import google.generativeai as genai
    
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel(
        model_name=settings.MODEL_NAME,
        system_instruction=settings.SYSTEM_INSTRUCTION
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
        'model_name': settings.MODEL_NAME
    }
    return render_template('index.html', config=config)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """ユーザー入力を受信しAI応答を返す"""
    try:
        message = request.json['message']
        
        if settings.AI_PROVIDER == 'openai':
            # OpenAI Responses APIを使用
            try:
                # まず通常のChat Completions APIを試す
                messages.append({"role": "user", "content": message})
                
                response = client.chat.completions.create(
                    model=settings.MODEL_NAME,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1000
                )
                
                assistant_message = response.choices[0].message.content
                messages.append({"role": "assistant", "content": assistant_message})
                
                return jsonify({'response': assistant_message})
                
            except AttributeError:
                # Responses APIが利用可能な場合はこちらを使用
                try:
                    response = client.responses.create(
                        model=settings.MODEL_NAME,
                        instructions=settings.SYSTEM_INSTRUCTION,
                        input=message
                    )
                    return jsonify({'response': response.output_text})
                except:
                    # フォールバック: 基本的なChat Completions API
                    response = client.chat.completions.create(
                        model=settings.MODEL_NAME,
                        messages=[
                            {"role": "system", "content": settings.SYSTEM_INSTRUCTION},
                            {"role": "user", "content": message}
                        ]
                    )
                    return jsonify({'response': response.choices[0].message.content})
                    
        elif settings.AI_PROVIDER == 'gemini':
            # Gemini APIを使用
            response = chat_session.send_message(message)
            return jsonify({'response': response.text})
            
    except Exception as e:
        # エラーハンドリング
        error_message = f"Error occurred: {str(e)}"
        print(f"[ERROR] {error_message}")
        print(traceback.format_exc())
        
        return jsonify({
            'error': error_message,
            'provider': settings.AI_PROVIDER,
            'model': settings.MODEL_NAME
        }), 500

if __name__ == '__main__':
    print(f"=== Avatar UI Core ===")
    print(f"AI Provider: {settings.AI_PROVIDER}")
    print(f"Model: {settings.MODEL_NAME}")
    print(f"Server running at: http://localhost:{settings.SERVER_PORT}")
    print(f"====================")
    
    app.run(debug=settings.DEBUG_MODE, port=settings.SERVER_PORT)