{
  [ ! -f .tmp/venv ] && (virtualenv -p python3 .tmp/venv)
  source .tmp/venv/bin/activate

  pip install -r requirements.txt
} &>/dev/null

python main.py "$1"
deactivate
