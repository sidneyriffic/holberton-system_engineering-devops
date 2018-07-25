# Basic web server and file transfer setup using Nginx

**0-transfer_file**: bash script that will transfer a file using scp.  
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY  
**1-install_nginx_on_web_server**: script that will install nginx on a server when run  
**3-redirect**: as 1, but script also sets up a redirect on /redirect_me  
**4-not_found_page_404**: as 3, but script also sets up a custom 404 page  
