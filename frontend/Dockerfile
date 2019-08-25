FROM node:8-alpine as build-stage
WORKDIR /app
COPY package.json /app/
RUN npm install package.json
COPY . /app/
RUN npm run build
FROM nginx:1.15
COPY --from=build-stage /app/build/ /usr/share/nginx/html
# Copy the default nginx.conf provided by tiangolo/node-frontend
COPY nginx.conf /etc/nginx/conf.d/default.conf