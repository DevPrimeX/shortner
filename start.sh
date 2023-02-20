if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Lucifer86790/shortner /shortner
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /shortner
fi
cd /shortner
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
