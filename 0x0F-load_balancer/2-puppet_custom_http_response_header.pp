#!/usr/bin/env bash
# Define a custom HTTP header response for Nginx
class custom_http_response_header {

  # Install package 'augeas-tools' required for manipulating Nginx configuration
  package { 'augeas-tools':
    ensure => installed,
  }

  # Define custom HTTP header configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "server {
  listen 80 default_server;
  listen [::]:80 default_server;

  server_name _;

  root /var/www/html;
  index index.html index.htm;

  location / {
    try_files \$uri \$uri/ =404;
  }

  # Add custom HTTP header
  add_header X-Served-By \$hostname;
}",
    notify  => Service['nginx'],
  }

  # Enable the custom HTTP header configuration
  exec { 'enable_custom_http_header':
    command => 'ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/',
    unless  => 'test -L /etc/nginx/sites-enabled/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }

  # Reload Nginx to apply changes
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

# Include the custom HTTP header configuration
include custom_http_response_header
