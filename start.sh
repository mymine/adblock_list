cd /root/adblock_list/
git pull origin master
/usr/bin/python3 /root/adblock_list/scripts/tools/adblock.py
git add -A
time=$(date "+%Y%m%d%H")
git commit -m "$time"
git push -u origin master