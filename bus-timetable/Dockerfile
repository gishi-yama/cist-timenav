FROM node:16-slim
COPY ./ /opt/app/
WORKDIR /opt/app
RUN npm install
CMD ["npm", "start", "dotenv_config_path_=/opt/app/.env"]