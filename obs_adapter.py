import obsws_python as obs
import os
from dotenv import load_dotenv

class OBSAdapter:
    def __init__(self) -> None:
        load_dotenv()  # .envファイルから環境変数を読み込む
        password = os.environ.get('OBS_WS_PASSWORD')  # OBS WebSocketのパスワード
        host = os.environ.get('OBS_WS_HOST')  # OBS WebSocketのホスト
        port = os.environ.get('OBS_WS_PORT')  # OBS WebSocketのポート
        # 必要な情報がなければエラー
        if password is None or host is None or port is None:
            raise Exception("OBSの設定がされていません")
        # OBS WebSocketに接続
        self.ws = obs.ReqClient(host=host, port=port, password=password)

    def set_question(self, text: str):
        # OBSのテキストソース"Question"に質問文を表示
        self.ws.set_input_settings(name="Question", settings={"text": text}, overlay=True)

    def set_answer(self, text: str):
        # OBSのテキストソース"Answer"に返答文を表示
        self.ws.set_input_settings(name="Answer", settings={"text": text}, overlay=True)

# テスト用: このファイルを直接実行した場合の動作
if __name__ == '__main__':
    obsAdapter = OBSAdapter()
    import random
    question_text = "Qustionの番号は" + str(random.randint(0, 100)) + "になりました"
    obsAdapter.set_question(question_text)
    answer_text = "Answerの番号は" + str(random.randint(0, 100)) + "になりました"
    obsAdapter.set_answer(answer_text)