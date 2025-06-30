import openai
import dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# OpenAIのAPIキーを環境変数から読み込む
# コメント行のインデント・スペースを修正し、VS Codeで正しく色付けされるようにしました。
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


class OpenAIAdapter:
    SAVE_PREVIOUS_CHAT_NUM = 5  # 過去の会話履歴を何件保存するか

    def __init__(self):
        # system_prompt.txtからキャラクター設定を読み込む
        with open("system_prompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.chat_log = []  # 会話履歴を保存するリスト

    def _create_message(self, role, message):
        # OpenAI API用のメッセージ形式に変換
        return {
            "role": role,
            "content": message
        }

    def create_chat(self, question):

        # LLMインスタンスを作成
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key= os.getenv("OPENAI_API_KEY"),  # if you prefer to pass api key in directly instaed of using env vars
            output_version="responses/v1"
            # base_url="...",
            # organization="...",
            # other params...
        )
        
        # ツールを定義（ここではweb_search_previewを使用）
        tool = {"type": "web_search_preview"}
        llm_with_tools = llm.bind_tools([tool])

        # メッセージリストを構築
        messages = [SystemMessage(content=self.system_prompt)]
        for c in self.chat_log:
            messages.append(HumanMessage(content=c["question"]))
            messages.append(AIMessage(content=c["answer"]))
        messages.append(HumanMessage(content=question))

        # LLMにメッセージリストを渡して回答を取得
        response = llm_with_tools.invoke(messages)
        answer = next(item["text"] for item in response.content if item.get("type") == "text")
        self._update_messages(question, answer)
        return answer

    def _get_messages(self):
        # system_promptを最初に追加
        system_message = self._create_message("system", self.system_prompt)
        messages = [system_message]
        for chat in self.chat_log:
            messages.append(self._create_message("user", chat["question"]))
            messages.append(self._create_message("assistant", chat["answer"]))
        return messages

    def _update_messages(self, question, answer):
        # チャットログを保存する
        self.chat_log.append({
            "question": question,
            "answer": answer
        })
        # チャットログがSAVE_PREVIOUS_CHAT_NUMを超えたら古いログを削除する
        if len(self.chat_log) > self.SAVE_PREVIOUS_CHAT_NUM:
            self.chat_log.pop(0)
        return True


if __name__ == "__main__":
    adapter = OpenAIAdapter()
    while True:
        question = input("質問を入力してください:")
        response_text = adapter.create_chat(question)
        print(response_text)
        print(adapter.chat_log)