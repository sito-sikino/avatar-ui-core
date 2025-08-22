from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import settings

# AI設定
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name=settings.MODEL_NAME,
    system_instruction=settings.SYSTEM_INSTRUCTION
)
chat = model.start_chat()

app = Flask(__name__)

@app.route('/')
def index():
    # ホーム画面表示とUI設定値を渡す
    config = {
        'typewriter_delay': settings.TYPEWRITER_DELAY_MS
    }
    return render_template('index.html', config=config)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    # ユーザーメッセージをAIに送信し応答を返す
    message = request.json['message']
    response = chat.send_message(message)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=settings.DEBUG_MODE, port=settings.SERVER_PORT)