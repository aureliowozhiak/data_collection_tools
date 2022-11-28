while :
do
  pkill python3
  sleep 150
  echo "Restarting...."

  python3 delete_messages.py
  echo "Deleting messages...."
  sleep 150
done