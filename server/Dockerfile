FROM node:20-alpine
WORKDIR /app

COPY package*.json ./
RUN npm install --omit=dev

COPY . .

ARG COMMIT_SHA=unknown
ENV GIT_COMMIT_SHA=$COMMIT_SHA

EXPOSE 5000
CMD ["node", "server.js"]