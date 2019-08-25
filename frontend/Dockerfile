FROM node:8-alpine
WORKDIR /app
COPY package.json .
RUN npm install package.json
COPY . .
CMD ["npm", "start"]