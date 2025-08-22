/**
 * アプリケーション設定モジュール
 * サーバーサイドから渡される設定値を管理
 */
export const createSettings = (config) => ({
    ...config,
    // アバター画像のパスを生成
    getAvatarImagePath: (isIdle = true) => 
        `/static/images/${isIdle ? config.avatarImageIdle : config.avatarImageTalk}`
});