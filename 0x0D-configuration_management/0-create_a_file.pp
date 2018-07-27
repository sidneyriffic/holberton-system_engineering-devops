#Creates /tmp/holberton with the given attributes
file { '/tmp/holberton':
  owner   => www-data,
  group   => www-data,
  mode    => '0744',
  content => 'I love Puppet'
}
