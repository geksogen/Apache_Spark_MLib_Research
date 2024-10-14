### Apache_Spark_Research

#### Requirements
* Ubuntu v22.04 (2CPU, 40GB HDD, 8Gb RAM)
* 3 VM

####Use Ansible install
```BASH
#Clone git repo
git clone https://github.com/geksogen/Apache_Spark_MLib_Research.git
cd Ansible_install
#add IP to host.ini
#ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i host.ini setup-spark-standalone.yml
```
####Master and workers
```BASH
cp /home/sp-user/spark/conf/spark-env.sh.template /home/sp-user/spark/conf/spark-env.sh # add to ansible
##############
nano /home/sp-user/spark/conf/spark-env.sh
#add to end line on the file
export SPARK_MASTER_HOST=<IP internal>
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

####On Master only
```BASH
#Add Workers or Slaves
cd /home/sp-user/spark
./sbin/start-all.sh
jps
```

###Run pyspark task
```BASH
sudo su sp-user
spark-submit --master spark://10.128.0.9:7077 /home/sp-user/spark/examples/src/main/python/pi.py 1000
git clone https://github.com/geksogen/Apache_Spark_MLib_Research.git
cd Python
spark-submit --master spark://10.128.0.9:7077 
```

####Copy ssh to node
```BASH
#node_1
sudo su sp-user
cd ~
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_1>
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_2>
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_3>
Enter passwd

#node_2
cd ~
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_1>
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_3>
Enter passwd

#node_3
cd ~
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_1>
ssh-copy-id -i ~/.ssh/id_rsa.pub sp-user@<node_2>
Enter passwd
```

1) Edit IP in host (Ansible)
2) Edit IP in task (Ansible) nano roles/spark/tasks/main.yml  
4) Coppy ssh key   (All hosts) sudo su sp-user&cd ~
3) cp spark-env    (All hosts) add to ansible

####Resources
[PySpark Tutorial](https://sparkbyexamples.com/pyspark-tutorial/)
[PySpark join two dataframes](https://www.geeksforgeeks.org/pyspark-join-types-join-two-dataframes/)
[Spark Standalone on Docker-Compose](https://dev.to/mvillarrealb/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-2021-update-6l4)
[Install Minio](https://www.digitalocean.com/community/tutorials/how-to-set-up-minio-object-storage-server-in-standalone-mode-on-ubuntu-20-04)
