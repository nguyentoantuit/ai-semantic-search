docker run -d -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=dF9xNTuZ433gAfG" opensearchproject/opensearch:latest

curl https://localhost:9200 -ku admin:dF9xNTuZ433gAfG
