FROM node:23-slim

WORKDIR /app

COPY server.js .
COPY index.html .
COPY package.json .

RUN npm install


EXPOSE 3000

CMD ["node", "server.js"]
