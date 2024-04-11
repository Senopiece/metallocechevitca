FROM node:18.20-alpine

WORKDIR /app
COPY . .

RUN npm ci
RUN npm run build

EXPOSE 3000

ENTRYPOINT node build
