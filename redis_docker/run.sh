docker rm -f redis
docker run -p 6379:6379 --name redis -v /home/znn/model/Neo4j_rasa/redis_docker/redis.conf:/etc/redis/redis.conf -v /home/znn/model/Neo4j_rasa/redis_docker/data:/data -d redis redis-server /etc/redis/redis.conf --appendonly yes           
