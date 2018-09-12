exec { 'fix phpp typo':
     command => 'sed -i "s/require_once[(] ABSPATH \. WPINC \'\/class-wp-locale\.phpp\' [)];/require_once[(] ABSPATH \. WPINC \'\/class-wp-locale\.phpp\' [)];/" /var/www/html/wp-settings.php',
     path => '/bin',
}
