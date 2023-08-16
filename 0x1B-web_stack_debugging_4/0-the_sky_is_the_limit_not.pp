# fixes requests failure by increasing ULIMIT.

exec {'fixing request failure':
  command => 'sudo sed -i "s/^ULIMIT.*/ULIMIT=\"-n 40999\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/:/usr/bin'
}

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/:/usr/bin'
}

