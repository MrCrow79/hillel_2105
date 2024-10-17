FROM python:3.12

# Встановлюємо необхідні залежності для Chrome
RUN apt-get update && apt-get install -y wget unzip curl gnupg

# Встановлюємо Google Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

RUN pip install webdriver-manager


CMD ["pytest", "-m", "swapi"]