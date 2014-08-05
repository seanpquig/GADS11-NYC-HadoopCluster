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
    
    hdfs dfs -copyFromLocal wordcounter.py
    hdfs dfs -mkdir input_wc
    hdfs dfs -copyFromLocal shakespeare.txt input_wc/shakespeare.txt
    hdfs dfs -copyFromLocal grep.py
    hdfs dfs -mkdir input_grep
    hdfs dfs -copyFromLocal grep_errors.log input_grep/grep_errors.log
    
    

Use fsck command for insight into how file is stored in HDFS.

    hdfs fsck /user/vagrant/input_wc/shakespeare.txt
    hdfs fsck /user/vagrant/input_grep/grep_errors.log


## Streaming MapReduce with Python

### Word count example (the hello world of MapReduce)

Let's expolore our data and Python script first

    less shakespeare.txt
    wc shakespeare.txt
    less wordcounter.py

Go to where the MapReduce JAR's live.  This is the standard format of MR programs (Java).

    ll /usr/lib/hadoop-mapreduce/
    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar

Let's run a MapReduce job!!

    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files "wordcounter.py" -mapper "python wordcounter.py map" -reducer "python wordcounter.py reduce" -input "input_wc" -output "output_wc"



### Distributed grep example



