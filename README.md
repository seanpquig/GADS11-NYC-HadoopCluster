# GADS11-NYC-HadoopCluster
=======

This project uses Vagrant to provision a 5 node virtual Hadoop cluster.

## Getting the cluster running

* Install Vagrant:  http://www.vagrantup.com/downloads
* Intall VirtualBox:  https://www.virtualbox.org/wiki/Downloads
* Clone this repo:  git clone https://github.com/seanpquig/GADS11-NYC-HadoopCluster.git  (make sure its outside of the general GADS11-NYC-Summer2014 repo)
* Open the root project folder and run "vagrant up"


## Basic HDFS usage
Confirm your Vagrant cluster is running.  
```vagrant status```

Log into the gateway client node.  
```vagrant ssh gw```

Go to lab folder.  
```cd /vagrant/lab```

Explore HDFS.
    hdfs dfs -ls /  
    hdfs dfs /user/vagrant


Copy file from client node into HDFS.
```hdfs dfs -copyFromLocal grep_errors.log words.txt```


