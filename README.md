ただのAPIができてしまった泣

# MCP Server Demo

これは、**スレッドごとの文脈を保持しながらOpenAI APIを使って応答を生成するAPIサーバー**のデモ実装です。  
FastAPI + Uvicorn によって構築されています。

## 📌 特徴

- 会話履歴（context）をスレッドごとに保持
- OpenAI GPTモデルを利用した応答生成
- Docker対応で手軽にデプロイ可能

## 🚀 使用技術

- Python 3.11
- FastAPI
- Uvicorn
- OpenAI API
- Docker

## 🛠️ エンドポイント

### `POST /mcp`

- **説明**: 会話メッセージを送信し、OpenAIの応答を返します。
- **リクエスト形式**:
```json
{
  "thread_id": "abc123",
  "messages": [
    {"role": "user", "content": "こんにちは！"}
  ],
  "context": {
    "temperature": 0.7
  }
}
```
- **レスポンス形式**:
```json
{
  "content": "こんにちは！どんなご用件ですか？"
}
```

## 🐳 Dockerでの実行

```bash
docker build -t mcp-server-demo .
docker run -p 8000:8000 mcp-server-demo
```
