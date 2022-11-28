while :
do
  pkill python3
  echo "Restarting...."
  sleep 50

  echo "50...."
  sleep 50

  echo "100...."
  sleep 50

  python3 delete_messages.py
  echo "Deleting messages...."
  sleep 150
done