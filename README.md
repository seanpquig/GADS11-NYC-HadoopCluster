# GADS11-NYC-HadoopCluster
=======

This project uses Vagrant to provision a 5 node virtual Hadoop cluster.

## Getting the cluster running

* Install Vagrant:  http://www.vagrantup.com/downloads
* Intall VirtualBox:  https://www.virtualbox.org/wiki/Downloads
* Clone this repo:  git clone https://github.com/seanpquig/GADS11-NYC-HadoopCluster.git  (make sure it's outside of the general GADS11-NYC-Summer2014 repo)
* Open the root project folder and run "vagrant up"


## Basic HDFS usage
Confirm your Vagrant cluster is running.  
```vagrant status```

Log into the gateway client node.  
```vagrant ssh gw```

Go to lab folder.  
    
    cd /vagrant/lab
    ls

Explore HDFS.

    hadoop fs -ls /
    hdfs dfs -ls /  
    hdfs dfs -ls /user/vagrant

Copy files from client node into HDFS. 

    hdfs dfs -copyFromLocal grep_errors.log
    hdfs dfs -copyFromLocal grep.py
    hdfs dfs -copyFromLocal shakespeare.txt
    hdfs dfs -copyFromLocal wordcounter.py
    hdfs dfs -ls /user/vagrant

Use fsck command for insight into how file is stored in HDFS.

    hdfs fsck /user/vagrant/grep_errors.log
    hdfs fsck /user/vagrant/shakespeare.txt


