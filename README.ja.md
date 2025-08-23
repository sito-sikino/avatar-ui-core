# Avatar UI Core

クラシックなターミナル調のUIコア。チャットUIからCLI統合まで拡張可能なプロジェクト基盤を提供します。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)

![Avatar UI Core Terminal Interface](docs/assets/avatar-ui_demo.gif)

## 特徴

- **ターミナルUI** - グリーンオンブラックの古典的ターミナルインターフェース
- **AIアバター** - 発話同期型のピクセルアートアバター表示
- **タイプライター効果** - 文字単位のリアルタイム表示アニメーション
- **サウンドエフェクト** - Web Audio APIによるタイピング音生成
- **完全な設定管理** - すべての動作パラメータを`.env`ファイルで一元管理

## 基本操作

1. **メッセージ送信**: 画面下部の入力欄にテキストを入力してEnterキー
2. **会話履歴**: 自動的にスクロールされる会話履歴を確認
3. **アバター**: AIの応答中はアバターが応答アニメーション

## クイックスタート

### 必要要件

- Python 3.8以上
- Google AI Studio APIキー（[取得はこちら](https://aistudio.google.com/app/apikey)）

### インストール手順

#### 1. プロジェクトの取得

```bash
# リポジトリのクローン（またはZIPダウンロード後に解凍）
git clone https://github.com/yourusername/avatar-ui-core.git
cd avatar-ui-core
```

#### 2. Python仮想環境の作成

仮想環境を使用することで、システムのPython環境を汚さずにプロジェクトを実行できます。

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化
# Linux/Mac:
source venv/bin/activate
# Windows (コマンドプロンプト):
venv\Scripts\activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1
```

仮想環境が有効化されると、ターミナルのプロンプトに`(venv)`が表示されます。

#### 3. 必要なパッケージのインストール

```bash
# requirements.txtに記載されたパッケージを一括インストール
pip install -r requirements.txt
```

### 設定

#### 1. 環境変数ファイルの準備

```bash
# テンプレートファイルをコピーして.envファイルを作成
cp .env.example .env
# Windows: copy .env.example .env
```

#### 2. APIキーの設定

テキストエディタで`.env`ファイルを開き、必須項目を設定：

```bash
# 必須項目のみ変更が必要（他の項目はデフォルト値で動作）
GEMINI_API_KEY=ここに取得したAPIキーを貼り付け
MODEL_NAME=gemini-2.0-flash  # または gemini-2.5-pro など
```

**重要**: `.env`ファイルには機密情報が含まれるため、絶対にGitにコミットしないでください。

### 起動

```bash
# アプリケーションの起動
python app.py
```

起動に成功すると以下のようなメッセージが表示されます：
```
 * Running on http://127.0.0.1:5000
```

ブラウザで `http://localhost:5000` にアクセスしてください。

## プロジェクト構造

```
avatar-ui-core/
├── app.py                  # Flaskアプリケーション本体
├── settings.py             # 設定管理モジュール
├── requirements.txt        # Python依存関係
├── .env.example           # 環境変数テンプレート
├── static/
│   ├── css/
│   │   └── style.css      # UIスタイル定義
│   ├── js/
│   │   ├── app.js         # メインエントリーポイント
│   │   ├── chat.js        # チャット機能
│   │   ├── animation.js   # アニメーション制御
│   │   ├── sound.js       # 音響効果
│   │   └── settings.js    # フロントエンド設定
│   └── images/
│       ├── idle.png       # アバター（静止）
│       └── talk.png       # アバター（発話）
└── templates/
    └── index.html         # HTMLテンプレート
```

**注意**: `docs/`フォルダには開発時のメモやアセットが含まれており、アプリケーション動作には影響しません。

## カスタマイズ方法

すべての設定は`.env`ファイルで調整できます。

### 1. アバターの変更

画像ファイルを差し替える
- `static/images/idle.png`: 静止時のアバター（推奨: 140x140px）
- `static/images/talk.png`: 発話時のアバター（推奨: 140x140px）

### 2. AIの人格設定
`.env`ファイルで以下の項目を編集：
```bash
AVATAR_NAME=Spectra
AVATAR_FULL_NAME=Spectra Communicator
SYSTEM_INSTRUCTION=あなたはSpectraというAIアシスタントです。技術的で直接的なスタイルで簡潔に応答してください。回答は短く要点を押さえたものにしてください。
```

### 3. UI動作の調整
`.env`ファイルで各種速度を調整：
```bash
# タイピング速度（ミリ秒、小さいほど高速）
TYPEWRITER_DELAY_MS=30

# 口パクアニメーション間隔（ミリ秒）
MOUTH_ANIMATION_INTERVAL_MS=100
```

### 4. サウンド設定
`.env`ファイルで音響効果をカスタマイズ：
```bash
BEEP_FREQUENCY_HZ=600   # 音の高さ（Hz）
BEEP_VOLUME=0.1         # 音量（0.0-1.0）
BEEP_DURATION_MS=30     # 音の長さ（ミリ秒）
```

**注意**: 設定変更後はアプリケーションの再起動が必要です。

## 環境変数一覧

| 変数名 | 説明 | デフォルト値 | 必須 |
|--------|------|-------------|------|
| `GEMINI_API_KEY` | Google Gemini APIキー | - | ✅ |
| `MODEL_NAME` | 使用するGeminiモデル | gemini-2.0-flash | ✅ |
| **サーバー設定** | | | |
| `SERVER_PORT` | サーバーポート番号 | 5000 | |
| `DEBUG_MODE` | デバッグモード有効化 | True | |
| **アバター設定** | | | |
| `AVATAR_NAME` | AIアシスタントの名前 | Spectra | |
| `AVATAR_FULL_NAME` | AIアシスタントのフルネーム | Spectra Communicator | |
| `AVATAR_IMAGE_IDLE` | 静止時のアバター画像 | idle.png | |
| `AVATAR_IMAGE_TALK` | 発話時のアバター画像 | talk.png | |
| **AI性格設定** | | | |
| `SYSTEM_INSTRUCTION` | AIの人格や応答スタイル | 技術的で簡潔な応答 | |
| **UI設定** | | | |
| `TYPEWRITER_DELAY_MS` | タイプライター効果の速度（ミリ秒） | 50 | |
| `MOUTH_ANIMATION_INTERVAL_MS` | 口パクアニメーション間隔（ミリ秒） | 150 | |
| **サウンド設定** | | | |
| `BEEP_FREQUENCY_HZ` | ビープ音の周波数（Hz） | 800 | |
| `BEEP_DURATION_MS` | ビープ音の長さ（ミリ秒） | 50 | |
| `BEEP_VOLUME` | ビープ音の音量（0.0-1.0） | 0.05 | |
| `BEEP_VOLUME_END` | ビープ音終了時の音量 | 0.01 | |

## 技術スタック

### バックエンド
- **Flask 3.0.0** - Webアプリケーションフレームワーク
- **google-generativeai 0.8.3** - Gemini API統合
- **python-dotenv 1.0.0** - 環境変数管理

### フロントエンド
- **ES6 Modules** - モジュール化されたJavaScript
- **Web Audio API** - ブラウザネイティブ音響生成
- **CSS3** - モダンなスタイリング
- **Fira Code** - プログラミング用等幅フォント

## ライセンス

MIT License - 詳細は[LICENSE](LICENSE)ファイルを参照

## クレジット

Developed by Sito Sikino

### 使用技術
- Google Gemini API
- Flask Framework  
- Fira Code Font

---

**注意**: このプロジェクトはエンタメ・創作目的で作成されています。本番環境での使用時は適切なセキュリティ対策を実施してください。