FROM python:3.11-slim

# 作業ディレクトリを指定
WORKDIR /var/www

# requirements.txt をコピーして依存インストール
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー（appフォルダ内のコード）
#COPY fastapi/ ./var/www/fastapi/