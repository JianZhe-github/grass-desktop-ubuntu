# 基础镜像
FROM ubuntu:22.04

# 环境变量设置
ENV DEBIAN_FRONTEND=noninteractive
ENV USER=root
ENV DISPLAY=:1

# 更新和安装所需的软件包，包括gdebi和Python
RUN apt-get update && apt-get install -y \
    supervisor \
    xfce4 \
    xfce4-goodies \
    x11vnc \
    xvfb \
    novnc \
    websockify \
    xterm \
    curl \
    wget \
    gdebi \
    locales \
    tzdata \
    tightvncserver \
    fonts-wqy-microhei \
    fonts-wqy-zenhei \
    fonts-arphic-ukai \
    fonts-arphic-uming \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libxss1 \
    libxt6 \
    libasound2 \
    libatk1.0-0 \
    libayatana-appindicator3-1 \
    libwebkit2gtk-4.1-0 \
    libpangocairo-1.0-0 \
    python3 \
    python3-pip \
    && pip install pyvirtualdisplay \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 安装 Firefox
RUN wget -O firefox-latest.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=zh-TW" \
    && tar xjf firefox-latest.tar.bz2 \
    && mv firefox /opt/firefox \
    && ln -s /opt/firefox/firefox /usr/local/bin/firefox \
    && rm firefox-latest.tar.bz2 \
    && update-alternatives --install /usr/bin/x-www-browser x-www-browser /usr/local/bin/firefox 100 \
    && update-alternatives --set x-www-browser /usr/local/bin/firefox \
    && update-alternatives --install /usr/bin/gnome-www-browser gnome-www-browser /usr/local/bin/firefox 100 \
    && update-alternatives --set gnome-www-browser /usr/local/bin/firefox


# 安装 Selenium 和 geckodriver
RUN pip3 install selenium \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz \
    && tar -xzf geckodriver-v0.32.0-linux64.tar.gz -C /usr/local/bin \
    && rm geckodriver-v0.32.0-linux64.tar.gz

# 设置桌面环境
RUN echo "xfce4-session" > ~/.xsession

# 复制Python脚本到容器中
COPY grass_desktop_install.py /root/grass_desktop_install.py

# 配置 supervisord
RUN mkdir -p /etc/supervisor/conf.d
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# 设置环境变量（比如数据库的用户名和密码）
ENV email=myuser
ENV password=mypassword

# 暴露端口
EXPOSE 5900 6080

# 启动 supervisord
CMD ["/usr/bin/supervisord"]
