# AITuber Python Programming Example

このリポジトリは「AITuberを作ってみたら生成AIプログラミングがよくわかった件」で紹介された、YouTubeライブ配信のコメントをAIキャラクターが読み上げて返答するサンプルプログラムです。

## 概要

YouTubeライブのコメントを取得し、OpenAIのAPIでAIキャラクター（蛍）が返答を生成し、VOICEVOXで音声合成、OBSで配信画面に表示、音声を再生する一連の流れを自動化します。

## 構成ファイル

- `run.py` : メイン実行ファイル。全体のループ処理を管理。
- `aituber_system.py` : システム全体の制御クラス。
- `openai_adapter.py` : OpenAI APIを用いた返答生成。
- `voicevox_adapter.py` : VOICEVOX APIを用いた音声合成。
- `obs_adapter.py` : OBS WebSocketを用いた配信画面のテキスト更新。
- `youtube_comment_adapter.py` : YouTubeライブのコメント取得。
- `play_sound.py` : 音声データの再生。
- `system_prompt.txt` : AIキャラクター「蛍」のプロンプト・キャラクター設定。
- `requirements.txt` : 必要なPythonパッケージ一覧。

## 必要な環境・依存パッケージ

- Python 3.8以上
- [VOICEVOXエンジン](https://voicevox.hiroshiba.jp/)（ローカルで起動しておく必要あり）
- OBS Studio + obs-websocket プラグイン
- YouTubeライブ配信環境

Pythonパッケージは`requirements.txt`で管理されています。

```
pip install -r requirements.txt
```

## .envファイルの設定

プロジェクトルートに`.env`ファイルを作成し、以下の内容を記載してください。

```
OPENAI_API_KEY=sk-...
YOUTUBE_VIDEO_ID=（配信中のYouTube動画ID）
OBS_WS_HOST=localhost
OBS_WS_PORT=4455
OBS_WS_PASSWORD=（OBS WebSocketのパスワード）
```

## 実行方法

1. VOICEVOXエンジンを起動する（デフォルト: http://127.0.0.1:50021/）
2. OBS Studioを起動し、WebSocketを有効化
3. `.env`ファイルを正しく設定
4. 必要なPythonパッケージをインストール
5. 下記コマンドで実行

```
python run.py
```

## 各アダプタの役割

- `YoutubeCommentAdapter` : YouTubeライブから最新コメントを取得
- `OpenAIAdapter` : コメントをもとにAI返答を生成
- `VoicevoxAdapter` : AI返答を音声合成
- `OBSAdapter` : OBSのテキストソースに質問・返答を表示
- `PlaySound` : 合成音声を再生

## 注意事項

- VOICEVOXエンジン、OBS Studio、YouTubeライブ配信は事前に準備・起動が必要です。
- 音声出力デバイス名（デフォルト: "CABLE Input"）は環境に合わせて`play_sound.py`で変更可能です。
- キャラクター設定は`system_prompt.txt`で編集できます。

## ライセンス・画像について

配信用画像は日経クロステックの該当記事（nkbpで始まるURL）を参照してください。

---

ご質問・不具合はIssue等でご連絡ください。