#fix phpp typo in file
exec { 'fix phpp typo':
  command => 'sed -i "s/ocale\.phpp/ocale\.php/" /var/www/html/wp-settings.php',
  path    => '/bin',
}
