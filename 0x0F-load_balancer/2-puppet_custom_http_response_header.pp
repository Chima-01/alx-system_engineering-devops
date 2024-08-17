# add custom header to nginx server

exec { 'update_server':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install_nginx'],
}


exec { 'install_nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['custom_header'],
}


exec { 'custom_header':
  provider    => shell,
  environment => ["Hostname=${::hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart server'],
}

exec { 'restart_server':
  provider => shell,
  command  => 'sudo service nginx restart',
}
