### Apache_Spark_Research

#### Requirements
* Ubuntu v22.04 (2CPU, 40GB HDD, 8Gb RAM)
* 3 VM

####Master and workers
```BASH
# public IP
sudo nano /etc/hosts
51.250.9.158 sp-master
89.169.129.85 sp-slave1
89.169.133.130 sp-slave2
#
sudo apt-get update
sudo apt install openjdk-8-jdk -y
sudo apt-get install scala -y
```
####Master and workers
```BASH
#Install Spark
wget https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
tar xvf spark-3.1.1-bin-hadoop3.2.tgz
sudo mv spark-3.1.1-bin-hadoop3.2 /usr/local/spark #directories for Spark
sudo nano ~/.bashrc
export PATH=$PATH:/usr/local/spark/bin
source ~/.bashrc
#################
cd /usr/local/spark/conf
cp spark-env.sh.template spark-env.sh
sudo nano spark-env.sh
#add to end line on the file
export SPARK_MASTER_HOST=<IP internal>
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
#
sudo nano /usr/local/spark/conf/slaves
sp-slave1
sp-slave2
```
####On Master only
```BASH
#Configure SSH IP External
sudo su
ssh-keygen
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# id_rsa.pub >> nano ~/.ssh/authorized_keys зайти и положить на каждую ноду ключик который сгенерировался на мастер ноде
```

####On Master only
```BASH
#Add Workers or Slaves
cd /usr/local/spark
./sbin/start-all.sh
jps
```
####Example for run for Spark
```BASH
#Calculation Pi
./bin/spark-submit --master spark://10.128.0.84:7077 /usr/local/spark/examples/src/main/python/pi.py 10000
```

####Use Ansible install
```BASH
#Clone git repo
git clone https://github.com/geksogen/Apache_Spark_MLib_Research.git
cd Ansible_install
#add IP to host.ini
ansible-playbook -i host.ini setup-spark-standalone.yml
```
####Master and workers
```BASH
# public IP
sudo nano /etc/hosts
<IP> sp-master
<IP> sp-slave1
<IP> sp-slave2
#
sudo nano ~/.bashrc
export PATH=$PATH:/usr/local/spark/bin
source ~/.bashrc
#
cd /usr/local/spark/conf
cp spark-env.sh.template spark-env.sh
sudo nano spark-env.sh
#add to end line on the file
export SPARK_MASTER_HOST=<IP internal>
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
#add slave
sudo nano /usr/local/spark/conf/slaves
sp-slave1
sp-slave2
```
####On Master only
```BASH
#Configure SSH IP External
sudo su
ssh-keygen
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# id_rsa.pub >> nano ~/.ssh/authorized_keys зайти и положить на каждую ноду ключик который сгенерировался на мастер ноде
```

####On Master only
```BASH
#Add Workers or Slaves
cd /usr/local/spark
./sbin/start-all.sh
jps
```

####For test
```BASH
****************node_1*********************************

sudo adduser sp-user
sudo usermod -aG sudo sp-user
su sp-user    # sudo su sp-user 

#no password
sudo nano /etc/sudoers
sp-user ALL=(ALL:ALL) ALL<>
sp-user ALL=(ALL:ALL) NOPASSWD: ALL
logout
sudo su sp-user #must be no password!!!  


****************node_2*********************************
sudo adduser sp-user
sudo usermod -aG sudo sp-user
su sp-user   # sudo su sp-user

#no password
sudo nano /etc/sudoers
sp-user ALL=(ALL:ALL) ALL
sp-user ALL=(ALL:ALL) NOPASSWD: ALL
logout
sudo su sp-user #must be no password!!!

**********************node_1*******************************
cd ~
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_2>
Enter passwd

**********************node_2********************************
cd ~
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_1> 
Enter passwd

```

####Resources
[PySpark Tutorial](https://sparkbyexamples.com/pyspark-tutorial/)
