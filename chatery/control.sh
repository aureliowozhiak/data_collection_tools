while :
do
  python3 -m chat
  sleep 1
  trap exit INT
  echo "Restarting...."
  trap exit INT
done
