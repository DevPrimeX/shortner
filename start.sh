if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Vijay14958/Proton-2 /Proton-2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Proton-2
fi
cd /Proton-2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
