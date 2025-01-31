# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# Playwrightをインストール
RUN playwright install
RUN playwright install-deps

# 必要なファイルをコンテナにコピー
COPY requirements.txt ./

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# ファイルをコンテナにコピー
COPY . .

# ポートを公開
EXPOSE 8080

# 実行コマンド
CMD ["python3", "main.py"]