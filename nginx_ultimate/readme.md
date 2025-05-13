## Introduction to Nginx

Nginx is a robust and efficient web server that handles is widely used in modern web development

Nginx employs a non-threaded, event-driven architecture.

This design allows Nginx to handle many more connections simultaneously, making it high suitable for
high traffic websites

### Forward Proxy VS Reverse Proxy
To understand Nginx's role as reverse proxy, it's helpful to first distinguish between a forward proxy and a reverse proxy.

- **Forward Proxy**: In a traditional HTTP connection, a client sends a request directly to a server. However, with a forward proxy (such as a VPN) the client sends the request to the proxy, which then forwards it to the server. The server is unaware of the original client; it only interacts with the proxy. This setup is useful for privacy and by passing georestrictions.

![image](../images/proxy_server.webp) <br>

- **Reverse Proxy**: In contrast, a reverse proxy sits between the client and multiple servers. The client sends a request to the reverse proxy, which then decides which server should handle the request.
