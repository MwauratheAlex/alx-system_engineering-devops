# kills a process named killmenow

exec {'execute_a_command':
  command => '/usr/bin/pkill -f killmenow',
}
