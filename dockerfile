# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt ./

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# Playwrightをインストール
RUN playwright install
RUN playwright install-deps

# ファイルをコンテナにコピー
COPY . .

# # 実行コマンド
# CMD ["python", "main.py"]