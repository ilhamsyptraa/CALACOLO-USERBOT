# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# RAM-UBOT
# Geez-UserBot
#yaudah iya

RUN git clone -b CALACOLO-USERBOT https://github.com/ilhamsyptraa/CALACOLO-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ilhamsyptraa/CALACOLO-USERBOT/CALACOLO-USERBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
