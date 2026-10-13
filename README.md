laba_2:
Команды запуска:
Ubuntu: sudo virsh start lab-vm
Проброс портов: ssh -L 8080:localhost:8080 -L 5000:localhost:5000 student@192.168.122.75
Пароль от логина student@192.168.122.75: 111
переходим в папку приложения: cd ~/docker-lab
запуск: docker compose up -d

переходим по адресу приложения:http://localhost:8080

схема:
(хостовая ОС) Windows 11 > WSL 2 (Ubuntu)  > KVM > ВМ: Ubuntu Server > Docker > контейнеры приложения 
