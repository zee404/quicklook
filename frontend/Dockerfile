FROM nginx:alpine

# Remove default config shipped with nginx image
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy frontend files
COPY src/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
