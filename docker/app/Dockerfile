FROM node:13-alpine

WORKDIR /app

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PASSWORD=password

COPY . .

RUN npm install

EXPOSE 3000

CMD ["node", "server.js"]
