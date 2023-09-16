# docker rm -f real-time_crypto_data_pipeline_using_kafka_docker-zookeeper-1
# docker rm -f real-time_crypto_data_pipeline_using_kafka_docker-broker-1
# docker rm -f real-time_crypto_data_pipeline_using_kafka_docker-producer-1
# docker rm -f real-time_crypto_data_pipeline_using_kafka_docker-consumer-1

docker rm -f $(docker ps -aq)
sleep 5
docker rmi -f $(docker images -q)

docker network rm real-time_crypto_data_pipeline_using_kafka_docker_default
