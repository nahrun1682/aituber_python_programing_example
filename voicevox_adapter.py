import json
import requests
import io
import soundfile


class VoicevoxAdapter:
    URL = 'http://127.0.0.1:50021/'  # VOICEVOXエンジンのURL
    # VOICEVOX APIは2回リクエストが必要（1回目:クエリ生成, 2回目:音声合成）
    def __init__(self) -> None:
        pass
    
    def __create_audio_query(self, text: str, speaker_id: int) -> json:
        # 1回目: テキストから音声合成用クエリを作成
        item_data = {
            'text': text,
            'speaker': speaker_id,
        }
        response = requests.post(self.URL + 'audio_query', params=item_data)
        return response.json()

    def __create_request_audio(self, query_data, speaker_id: int) -> bytes:
        # 2回目: クエリデータを使って音声データ（wav）を生成
        a_params = {
            'speaker': speaker_id,
        }
        headers = {"accept": "audio/wav", "Content-Type": "application/json"}
        res = requests.post(self.URL + 'synthesis', params=a_params, data=json.dumps(query_data), headers=headers)
        print(res.status_code)  # ステータスコードで通信成功を確認
        return res.content

    def get_voice(self, text: str):
        # テキストから音声データ（numpy配列）とサンプリングレートを返す
        speaker_id = 3  # 話者ID（VOICEVOXのキャラクター番号）
        query_data = self.__create_audio_query(text, speaker_id=speaker_id)
        audio_bytes = self.__create_request_audio(query_data, speaker_id=speaker_id)
        audio_stream = io.BytesIO(audio_bytes)
        data, sample_rate = soundfile.read(audio_stream)
        return data, sample_rate


if __name__ == "__main__":
    # テスト用: "こんにちは" を音声合成してサンプリングレートを表示
    voicevox = VoicevoxAdapter()
    data, sample_rate = voicevox.get_voice("こんにちは")
    print(sample_rate)