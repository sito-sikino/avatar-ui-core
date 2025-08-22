/**
 * チャット機能モジュール
 * メッセージの送受信とUI更新を管理
 */
export class ChatManager {
    constructor(settings, animationManager) {
        this.settings = settings;
        this.animationManager = animationManager;
        this.output = document.getElementById('output');
        this.input = document.getElementById('input');
        
        this.initEventListeners();
    }

    // イベントリスナー初期化
    initEventListeners() {
        this.input.addEventListener('keypress', async (e) => {
            if (e.key === 'Enter' && this.input.value.trim()) {
                await this.sendMessage(this.input.value);
                this.input.value = '';
            }
        });
    }

    // メッセージ送信
    async sendMessage(message) {
        // ユーザーメッセージを表示
        this.addLine(message, 'user');
        
        try {
            // AIに送信
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message})
            });
            
            const data = await response.json();
            
            // AIレスポンスをタイプライター効果で表示
            await this.addLine(data.response, 'ai');
        } catch (error) {
            console.error('Chat error:', error);
            this.addLine('エラーが発生しました。再試行してください。', 'system');
        }
    }

    // メッセージを画面に追加
    async addLine(text, type) {
        const line = document.createElement('div');
        line.className = 'line ' + type;
        
        if (type === 'user') {
            line.innerHTML = `<span class="user-prompt">USER&gt;</span> ${text}`;
            this.output.appendChild(line);
            this.scrollToBottom();
        } else if (type === 'ai') {
            // AIメッセージはタイプライター演出
            line.innerHTML = `<span class="ai-prompt">${this.settings.avatarName}&gt;</span> <span class="ai-text"></span>`;
            this.output.appendChild(line);
            
            const aiTextElement = line.querySelector('.ai-text');
            await this.animationManager.typeWriter(aiTextElement, text);
        } else {
            // system メッセージなど
            line.textContent = text;
            this.output.appendChild(line);
            this.scrollToBottom();
        }
    }

    // チャットエリアを最下部にスクロール
    scrollToBottom() {
        this.output.scrollTop = this.output.scrollHeight;
    }
}