# real-time_crypto_data_pipeline_using_docker_kafka_S3_and_Snowflake

## Introduction 
In this project, you will execute an End-To-End Data Engineering Project on Real-Time crypto Data using Kafka and make all service dockerize.

I am using  Apache Kafka to produce and consume scraped data.

In this project, I've created a real-time data pipeline that utilizes Kafka to scrape, process, and load data onto S3 in JSON format. With a producer-consumer architecture, I ensure that the data is in the right format for loading onto S3 by performing minor transformations while consuming it.The most interesting thing is that i dockerized all service and run all
through docker.

<!-- But that's not all - I've also used AWS crawler to crawl the data and generate a schema catalog. Athena utilizes this catalog, allowing me to query the data directly from S3 without loading it first. This saves time and resources and enables me to get insights from the data much faster! -->

Moreover, I've connected S3 with Snowflake using Snowpipe. As data is loaded onto S3, a SNS notification is sent to Snowpipe, which then automatically starts loading the data into Snowflake. This makes data loading a seamless and automated process, freeing up time for other important tasks lile querry and analysis. 

## Architecture 
![kafka_proj](docker.png)

## Technology Used
- Programming Language - Python
- Amazon Web Service (AWS)
1. S3 (Simple Storage Service)
2. EC2 or Local Machine
3. Apache Kafka
4. Snowflake
5. Docker

## Follow the below Process  :  

    1)First step is to create S3 bucket:

<img src="./images/buc1.png">

<img src="./images/buck2.png">

<img src="./images/buc3.png">

<br>
   
    Now if you want work on ec2 instance machine then first create ec2 instance machine if not want to run ec2 then move forward

<img src="./images/ec1.png">

<br>

    Then click to launch instances
<img src="./images/ec2.png">
<img src="./images/ec3.png">
<img src="./images/ec4.png">
<br>

    Then click on create new keypair
<br>    
<img src="./images/ec5.png">

<br>

    write pair name
    
<img src="./images/ec7.png"> 

    Then click to create and mydata.pem file download in computer.Put this file to this project folder.
 

<img src="./images/ec9.png">
<img src="./images/ec10.png">

    click to launch instance and instance create
<br>

    Click to connect to your instance --> connect to instance

<img src="./images/ec11.png">

<img src="./images/ec12.png">

<br>

    Go to vscode and do as in pic

<img src="./images/ec18.png">
<img src="./images/ec19.png">

<br>

<img src="./images/ec13.png">
<br>

    go to security then  inbound rules go to security groups and click link 

<img src="./images/ec14.png">

<br>

    Then click on edit inbound rules
   
    
<img src="./images/ec15.png">   

<img src="./images/ec16.png">   

<br>
    
    Then click on Add rule and select as i do below pic and click on save rules

<img src="./images/ec17.png"> 

<br>

    Now go back vs code terminal where your instance connect
<img src="./images/ec18.png">
<img src="./images/ec19.png">

    Note: EC2 part end
<br>
   

    Now do the following the below steps (for both local and ec2 applicable)
<br> 

    ---   Download Docker   ----

    https://docs.docker.com/engine/install/ubuntu/

    https://docs.docker.com/get-docker/



<br>
    Now go to your project folder terminal 

    ./start_app.sh

    then your code is running 

     for stop all code 
    ./stop_app.sh

    Note: if docker not work in start or stop sh then put sudo before  docker everywhere.
