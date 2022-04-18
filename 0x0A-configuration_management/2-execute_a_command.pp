# Execute a command

exec { 'Execute a command':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => 'shell',
  command  => 'pkill killmenow',
}
