# Apache_Spark_MLib_Research
* Ubuntu v22.04 (2CPU, 40GB HDD, 8Gb RAM)
#### Pre config VM
```Bash
sudo apt update
sudo apt upgrade
sudo apt -y install python3-pip

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
## Install Jupiter HUB (not working)
```Bash
git clone https://collaborating.tuhh.de/cmk3624/minimal-jupyterhub-docker-config.git
cd minimal-jupyterhub-docker-config/
python3 -m pip install -r ./requirements.txt
sh start.sh 
```

## Install Jupiter HUB
```Bash
docker run -it -p 8000:8000 --name jhubcontainer jupyterhub/jupyterhub bash
#docker run -d --rm -p 8000:8000 --name jupyterhub jupyterhub/jupyterhub
```

## Configure JypiterHUb (inside container)
```Bash
#docker exec -it jupyterhub bash
apt update
apt-get install npm nodejs python3 python3-pip git nano wget
python3 -m pip install jupyterhub notebook jupyterlab
#npm install -g configurable-http-proxy
cd /home
git clone https://github.com/jupyterhub/nativeauthenticator.git
cd nativeauthenticator
pip3 install -e .
mkdir /etc/jupyterhub  
cd /etc/jupyterhub
jupyterhub --generate-config -f jupyterhub_config.py
nano jupyterhub_config.py
```
insert to head
```Python
import pwd, subprocess

c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'

c.Authenticator.admin_users = {'admin'}

def pre_spawn_hook(spawner):
    username = spawner.user.name
    try:
        pwd.getpwnam(username)
    except KeyError:
        subprocess.check_call(['useradd', '-ms', '/bin/bash', username])
c.Spawner.pre_spawn_hook = pre_spawn_hook
c.Spawner.default_url = '/lab'
```

```Bash
jupyterhub -f /etc/jupyterhub/jupyterhub_config.py
```

go to http://IP:8000/hub/signup

### Install Apache Pyspark (inside container)
```Bash
apt install default-jdk
wget wget https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
tar xvf spark-3.5.0-bin-hadoop3.tgz
mv spark-3.5.0-bin-hadoop3/ /opt/spark
nano ~/.profile
```
```Bash
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=/usr/bin/python3
```
```Bash
source ~/.profile
spark-shell --version
#pyspark
```
