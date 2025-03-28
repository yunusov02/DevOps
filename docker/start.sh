# Start Mongo DB Container
docker run -p 27017:27017 -d \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=password \
    --name mongodb \
    --net mongo-network \
    mongo

# Start Mongo Express Container

docker run -d \
    -p 8081:8081 \
    -e ME_CONFIG_BASICAUTH_USERNAME=teraxiom \
    -e ME_CONFIG_BASICAUTH_PASSWORD=teraxiom \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
    -e ME_CONFIG_MONGODB_SERVER=mongodb \
    --name mongo-express \
    --net mongo-network \
    mongo-express


