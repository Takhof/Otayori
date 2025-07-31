# 💌 おたより掲示板アプリ

Dockerの練習用に作った、超シンプルなFlask掲示板アプリです！

---

## 🌸 機能

- メッセージ投稿フォーム
- 投稿内容をファイル（`messages.txt`）に保存
- Dockerで動かせる！
- `docker-compose` でワンクリック起動！

---

## 🛠️ 開発環境

- Python 3.11
- Flask
- Docker
- Docker Compose

---

## 🚀 起動方法

```bash
# イメージのビルドと起動
docker-compose up --build
ブラウザで → http://localhost:5000 にアクセス！

📂 フォルダ構成
cpp
Copy
Edit
letter-board-app/
├── app/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── messages.txt
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md