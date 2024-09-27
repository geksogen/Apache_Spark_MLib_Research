# Apache_Spark_MLib_Research



## Requirements
* Ubuntu v22.04 (2CPU, 40GB HDD, 8Gb RAM)
* 4 VM 

## Install Multi-node Spark Cluster (Standalone)
### Setup Master Node
```BASH
sudo apt update
# add node host names into /etc/hosts
sudo nano /etc/hosts
10.128.0.106 spark-master
10.128.0.111 spark-worker1
10.128.0.36  spark-worker2
10.128.0.104 spark-worker3
# install asdf
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.13.0
# configure asdf
echo ". $HOME/.asdf/asdf.sh" >> ~/.bashrc
source ~/.bashrc
# install java, scala
asdf plugin add java
asdf install java openjdk-11
asdf global java openjdk-11
# set java home
. ~/.asdf/plugins/java/set-java-home.bash
# install spark
wget https://archive.apache.org/dist/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz
tar xvf spark-3.5.3-bin-hadoop3.tgz
mv spark-3.5.3-bin-hadoop3 spark-3.0.0
cd spark-3.0.0
# set spark home and jave home
nano ~/.bashrc
export SPARK_HOME=$HOME/spark-3.0.0
export PATH=$PATH:$SPARK_HOME/bin
# configure spark env in `conf/spark-env.sh` file
# there is template of the `spark-env.sh` file `conf/spark-env.sh.template`
cp conf/spark-env.sh.template conf/spark-env.sh
# define master node host and java home
nano conf/spark-env.sh
export SPARK_MASTER_HOST=172.31.1.30 # change to current IP
export JAVA_HOME=/home/ubuntu/.asdf/installs/java/openjdk-11
# define slave node details in `conf/slaves` file
nano conf/slaves
spark-worker1
# generate ssh key pair for master node 
ssh-keygen
# following is the public key
cat ~/.ssh/id_rsa.pub
```

### Setup each  Slave Node
```BASH
# add node host names into /etc/hosts
sudo nano /etc/hosts
10.128.0.106 spark-master
10.128.0.111 spark-worker1
10.128.0.36  spark-worker2
10.128.0.104 spark-worker3
# install asdf
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.13.0
# configure asdf
echo ". $HOME/.asdf/asdf.sh" >> ~/.bashrc
source ~/.bashrc
# install java, scala
asdf plugin add java
asdf install java openjdk-11
asdf global java openjdk-11
# set java home
. ~/.asdf/plugins/java/set-java-home.bash
# install spark
wget https://archive.apache.org/dist/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz
tar xvf spark-3.5.3-bin-hadoop3.tgz
mv spark-3.5.3-bin-hadoop3 spark-3.0.0
cd spark-3.0.0
# set spark home and jave home
nano ~/.bashrc
export SPARK_HOME=$HOME/spark-3.0.0
export PATH=$PATH:$SPARK_HOME/bin
# configure spark env in `conf/spark-env.sh` file
# there is template of the `spark-env.sh` file `conf/spark-env.sh.template`
cp conf/spark-env.sh.template conf/spark-env.sh
# define master node host and java home
nano conf/spark-env.sh
export SPARK_MASTER_HOST=172.31.1.30 # change to current IP
export JAVA_HOME=/home/ubuntu/.asdf/installs/java/openjdk-11
# define slave node details in `conf/slaves` file
nano conf/slaves
spark-worker1
# copy the public key of the master node into each worker nodes' `~/.ssh/authorized_keys` file
# following is the content of the `~/.ssh/authorized_keys` file in each worker node
nano ~/.ssh/authorized_keys
```
### Start Cluster on Master Node
```BASH
# start cluster
# this command will start 1 master node and 4 worker nodes according to the `slaves` config 
cd ./spark-3.0.0/sbin
./start-all.sh
```
###*** external IP********************************************
#Master and workers
```BASH
sudo nano /etc/hosts
51.250.9.158 sp-master
89.169.129.85 sp-slave1
89.169.133.130 sp-slave2
#
sudo apt-get update
sudo apt install openjdk-8-jdk -y
sudo apt-get install scala -y
```
#On Master only
```BASH
#Configure SSH IP External
sudo su
ssh-keygen
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# id_rsa.pub >> nano root/.ssh/authorized_keys зайти и положить на каждую ноду ключик который сгенерировался на мастер ноде
```
#Master and workers
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

#On Master only
```BASH
#Add Workers or Slaves
cd /usr/local/spark
./sbin/start-all.sh
jps
```
