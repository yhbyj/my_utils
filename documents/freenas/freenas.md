#FreeNAS 手册  
## RancherOS on FreeNAS-11.2-U7 
参考：  
[玩转Freenas系统06——freenas下使用docker（配置RancherOS/Portainer）](https://www.bilibili.com/video/BV1NJ411Q7Hw)
[cloud-config.yml](https://gist.githubusercontent.com/superseb/15aada95f6f2fbacc1af7a442c767cce/raw/158c8d0161ec6416aa558d3dad4d1e2afb026d89/cloud-config.yml)
### 修改IP地址
```commandline
sudo ros config set rancher.network.interfaces.eth0.address 192.168.41.11/24
sudo ros config set rancher.network.interfaces.eth0.gateway 192.168.41.1
sudo ros config set rancher.network.interfaces.eth0.mtu 1500
sudo ros config set rancher.network.interfaces.eth0.dhcp false
sudo ros config set rancher.network.interfaces.eth0.dns.nameservers "['60.191.244.2', '60.191.244.5']"
sudo reboot
```
### NFS挂载  
```commandline
sudo -i
cd /var/lib/rancher/conf/cloud-config.d
vi cloud-config.yml
``` 
### container web ui management: portainer  
```commandline
sudo -i
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v /mnt/container/portainer:/data --restart always --name portainer portainer/portainer
```
## mysql on docker on RancherOS  
### 配置docker 
```commandline
sudo -i
vi /etc/docker/daemon.json
```
```text
{
"registry-mirrors": ["http://hub-mirror.c.163.com",
"https://docker.mirrors.ustc.edu.cn"]
}
```
### 随宿主机启动
```commandline
sudo docker run --name mysql57-demo-3306 -p 3306:3306 -v /mnt/container/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --restart=always -d mysql:5.7
```
### 修改配置
```commandline
docker exec -it mysql57-demo-3306 bash
mysql -uroot -p123456
```
```mysql-sql
grant all on *.* to 'root'@'192.168.41.%' identified by '123456' WITH GRANT OPTION;
flush privileges;
```
### 测试（(192.168.41.X/24)）
```commandline
docker run -it --rm mysql:5.7 mysql -h192.168.41.11 -uroot -p123456
```
## jupyter/scipy-notebook on docker on RancherOS
### 启动
```commandline
sudo docker run -d -p 10000:8888 -v /mnt/container/jupyter-scipy-notebook:/home/jovyan/work --name jupyter-scipy-notebook-10000 jupyter/scipy-notebook
```
### 测试（查看端口和登录口令）
```commandline
docker port jupyter-scipy-notebook-10000
docker logs --tail 3 jupyter-scipy-notebook-10000
```