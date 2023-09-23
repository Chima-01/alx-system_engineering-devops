# kill a processs named killmenow

exec {'killer':
  command => '/usr/bin/pkill killmenow',
}
