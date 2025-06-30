import time
from aituber_system import AITuberSystem
import traceback

# メイン処理の開始
# AITuberSystemクラスを使って、YouTubeコメントの取得・AI応答・音声合成・配信画面表示・音声再生を自動で繰り返します。

aituber_system = AITuberSystem()  # システム全体のインスタンスを作成

while True:
    try:
        # コメント取得→AI応答→音声合成→配信画面表示→音声再生を1回実行
        aituber_system.talk_with_comment()
        time.sleep(5)  # 5秒待ってから次のコメントを取得
    except Exception as e:
        # 何かエラーが発生した場合は詳細を表示して終了
        print("エラーが発生しました")
        print(traceback.format_exc())
        print(e)
        exit(200)