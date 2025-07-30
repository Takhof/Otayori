# ① ベースイメージを指定
FROM python:3.11-slim

# ② 作業ディレクトリをつくる
WORKDIR /app

# ③ 必要ファイルをコピー
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ④ アプリの中身もコピー
COPY app/ ./app

# ⑤ Flask起動に必要な環境変数
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# ⑥ ポートを開ける（Flaskのデフォルト）
EXPOSE 5000

# ⑦ Flaskを起動するコマンド
CMD ["flask", "run"]