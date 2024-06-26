#!/usr/bin/env bash
# Define a custom HTTP header response for Nginx using puppet

# install and configure nginx
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure => installed,
}
-> file_line { 'header_served_by':
  path  => '/etc/nginx/sites-available/default',
  match => '^server {',
  line  => "server {\n\tadd_header X-Served-By \"${hostname}\";",
  multiple => false,
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
