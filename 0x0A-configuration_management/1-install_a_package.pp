# puppet manifest, install flask with pip3
package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
