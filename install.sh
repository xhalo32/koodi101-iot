#write out current crontab
crontab -l > mycron

#echo new cron into cron file
echo "00 09 * * 1-5 $PWD" >> mycron

#install new cron file
crontab mycron
rm mycron

