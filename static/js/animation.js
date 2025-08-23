/**
 * アニメーション管理モジュール
 * タイプライター効果と口パクアニメーションを管理
 */
export class AnimationManager {
    constructor(settings, soundManager) {
        this.settings = settings;
        this.soundManager = soundManager;
        this.talkingInterval = null;
        this.avatarImg = document.getElementById('avatar-img');
        this.output = document.getElementById('output');
    }

    // 口パクアニメーション開始
    startMouthAnimation() {
        if (this.talkingInterval) {
            this.stopMouthAnimation();
        }

        let mouthOpen = false;
        this.talkingInterval = setInterval(() => {
            const imagePath = this.settings.getAvatarImagePath(!mouthOpen);
            this.avatarImg.src = imagePath;
            mouthOpen = !mouthOpen;
        }, this.settings.mouthAnimationInterval);
    }

    // 口パクアニメーション停止
    stopMouthAnimation() {
        if (this.talkingInterval) {
            clearInterval(this.talkingInterval);
            this.talkingInterval = null;
        }
        // アイドル状態に戻す
        this.avatarImg.src = this.settings.getAvatarImagePath(true);
    }

    // タイプライター効果
    typeWriter(element, text) {
        return new Promise((resolve) => {
            let i = 0;
            
            // 口パクアニメーション開始
            this.startMouthAnimation();
            
            const type = () => {
                if (i < text.length) {
                    element.textContent += text.charAt(i++);
                    this.output.scrollTop = this.output.scrollHeight;
                    
                    // スペース以外で音を鳴らす
                    if (text.charAt(i-1) !== ' ') {
                        this.soundManager.playTypeSound();
                    }
                    
                    setTimeout(type, this.settings.typewriterDelay);
                } else {
                    // 完了時：口を閉じる
                    this.stopMouthAnimation();
                    resolve();
                }
            };
            
            type();
        });
    }
}