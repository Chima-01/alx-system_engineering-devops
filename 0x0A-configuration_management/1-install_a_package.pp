# puppet manifest, install flask from pip3

package { 'pip':
  ensure  => 'installed',
}

exec { 'flask':
  command => '/usr/bin/pip install flask',
  require => Package['pip'],
}
