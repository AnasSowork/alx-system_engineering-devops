#!/usr/bin/env bash
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  content => "
server {
    listen 80;
    server_name _;

    location / {
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 /;
    }
}",
  require => Package['nginx'],
}

# Enable Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}
