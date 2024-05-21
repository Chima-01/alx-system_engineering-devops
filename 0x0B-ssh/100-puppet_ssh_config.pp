# Puppet manifest to connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  content => [
    '#   PasswordAuthentication no',
    '#   IdentityFile ~/.ssh/school',
  ],
}
