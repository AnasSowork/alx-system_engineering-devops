# Install Flask 2.1.1
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
