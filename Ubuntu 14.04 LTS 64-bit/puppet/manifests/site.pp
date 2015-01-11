exec {"apt-get update":
    path => "/usr/bin",
}

class { 'java':
  distribution => 'jre',
}

include stdlib, java
