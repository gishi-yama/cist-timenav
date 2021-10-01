FROM node:16-slim
COPY ./ /opt/app/
WORKDIR /opt/app
RUN npm install
ENV MINER miner:8080
CMD ["npm", "start"]