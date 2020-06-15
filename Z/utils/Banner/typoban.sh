
#!/bin/bash

clear
rm -f /data/data/com.termux/files/usr/etc/bash.bashrc
figlet -f big Banner | lolcat
cyan='\e[0;36m'
lightgreen='\e[1;32m'
red='\e[1;31m'
yellow='\e[1;33m'
echo -e $lightgreen "\e[1mSecurity Help For Ethical Hackers... "
echo " "
echo "Tg: @Termuxtop"
echo "Dev: @overlamer2130 && @nkitas"
echo " "
echo -e "\e[1m\e[33m\nWhat is Your \e[31m \e[33mName\e[32m :\n\n "
read ps1
echo
echo "PS1='\[\e[31m\]┌─[\[\e[37m\]\T\[\e[31m\]]─────\e[1;98m[$ps1]\e[0;31m───[\#]\n|\n\e[0;31m└─[\[\e[31m\]\e[0;35m\W\[\e[31m\]]────►\e[1;93m'" > ps1.txt
echo " "
echo -e "\e[1m\e[33m\nWhat is Your \e[31mBanner \e[33mName\e[32m :\n\n "
read varbanner
echo
echo "toilet -f big '    $varbanner' -F gay | lolcat" > 84nn3r.txt
echo
echo "clear" > cl34r.txt
cat "cl34r.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
cat "84nn3r.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
cat "ps1.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
echo " "
echo -e "\e[0;36m\nУспешно!!"
