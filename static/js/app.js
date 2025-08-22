/**
 * メインアプリケーションエントリーポイント
 * 各モジュールを初期化し、アプリケーションを起動
 */
import { createSettings } from './settings.js';
import { SoundManager } from './sound.js';
import { AnimationManager } from './animation.js';
import { ChatManager } from './chat.js';

// DOMロード完了後にアプリケーション初期化
document.addEventListener('DOMContentLoaded', () => {
    // グローバル変数appConfigはindex.htmlで定義される
    if (typeof appConfig !== 'undefined') {
        const settings = createSettings(appConfig);
        const soundManager = new SoundManager(settings);
        const animationManager = new AnimationManager(settings, soundManager);
        window.chatManager = new ChatManager(settings, animationManager);
    } else {
        console.error('App config not found');
    }
});