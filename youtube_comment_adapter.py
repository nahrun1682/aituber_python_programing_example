import pytchat
import json


class YoutubeCommentAdapter:
    def __init__(self, video_id) -> None:
        # YouTubeライブの動画IDからチャット取得用のインスタンスを作成
        self.chat = pytchat.create(video_id=video_id, interruptable=False)

    def get_comment(self):
        # コメントを一括で取得
        comments = self.__get_comments()
        if comments is None:
            return None
        comment = comments[-1]  # 最新のコメントを取得
        # コメント情報の中から実際のコメント文だけを取り出す
        message = comment.get("message")
        return message

    def __get_comments(self):
        # チャットが生きているか確認
        if self.chat.is_alive() is False:
            print("開始してません")
            return None
        # コメント一覧をJSON形式で取得
        comments = json.loads(self.chat.get().json())
        if comments == []:
            print("コメントが取得できませんでした")
            return None
        return comments


if __name__ == "__main__":
    # テスト用: 動画IDを指定してコメントを取得
    import time

    video_id = "jfKfPfyJRdk"
    chat = YoutubeCommentAdapter(video_id)
    time.sleep(1)  # コメント取得のために少し待つ
    print(chat.get_comment())