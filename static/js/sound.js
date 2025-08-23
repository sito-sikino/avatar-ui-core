/**
 * サウンド生成・再生モジュール
 * タイプライター効果音の生成と再生を管理
 */
export class SoundManager {
    constructor(settings) {
        this.settings = settings;
        this.audioContext = null;
        this.initAudioContext();
    }

    // Web Audio Context初期化
    initAudioContext() {
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        } catch (error) {
            // Audio未対応環境では無音で続行
        }
    }

    // タイプライター効果音を再生
    playTypeSound() {
        if (!this.audioContext) return;

        try {
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            oscillator.type = 'square';  // 矩形波
            oscillator.frequency.setValueAtTime(
                this.settings.beepFrequency, 
                this.audioContext.currentTime
            );
            
            gainNode.gain.setValueAtTime(
                this.settings.beepVolume, 
                this.audioContext.currentTime
            );
            const durationInSeconds = this.settings.beepDuration / 1000;  // ms→秒変換
            gainNode.gain.exponentialRampToValueAtTime(
                this.settings.beepVolumeEnd, 
                this.audioContext.currentTime + durationInSeconds
            );
            
            oscillator.start(this.audioContext.currentTime);
            oscillator.stop(this.audioContext.currentTime + durationInSeconds);
        } catch (e) {
            // 音声再生エラーは無視
        }
    }
}