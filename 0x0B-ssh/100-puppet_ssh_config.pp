# configure ~/.ssh/config using puppet

file { '/root/.ssh/config':
  ensure  => present,
  content => "Host 54.87.178.219\n\
	      IdentityFile ~/.ssh/school\n\
	      PasswordAuthentication no",
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
}
