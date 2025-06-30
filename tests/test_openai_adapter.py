import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from openai_adapter import OpenAIAdapter
import pytest
from unittest.mock import patch
from openai_adapter import OpenAIAdapter

def test_create_chat_real_api():
    adapter = OpenAIAdapter()
    question = "こんにちは"
    answer = adapter.create_chat(question)
    # 返答が空でないことを確認
    assert isinstance(answer, str)
    assert len(answer) > 0
    print("返答:", answer)
    
@patch("openai_adapter.openai.ChatCompletion.create")
def test_chat_log_limit(mock_create):
    mock_create.return_value = {
        "choices": [
            {"message": {"content": "返答"}}
        ]
    }
    adapter = OpenAIAdapter()
    # チャット履歴の最大数+2回質問
    for i in range(adapter.SAVE_PREVIOUS_CHAT_NUM + 2):
        adapter.create_chat(f"Q{i}")
    # 履歴が最大数に収まっているか
    assert len(adapter.chat_log) == adapter.SAVE_PREVIOUS_CHAT_NUM