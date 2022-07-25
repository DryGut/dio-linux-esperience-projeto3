<html>
  <head>
    <title>Projeto de Microsserviços</title>
  </head>
  <body>
    <?php
        ini_set("display_errors", 1);

        echo 'Versao Atual do PHP: ' . phpversion() . '<br>';

        //iniciando a conexão
        require_once 'dbconfig.php';
        $valor_rand1 = strtoupper(substr(bin2hex(random_bytes(4)), 1));
        $host_name = gethostname();

        $sql = "INSERT INTO clientes (nome, sobrenome, endereco, host) VALUES ('$valor_rand1', '$valor_rand1', '$valor_rand1', '$host_name')";

        if($db->exec($sql) === TRUE){
          echo "New record created successfully";
        } else {
          echo "Error: " . $db->error;
        }
      ?>
  </body>
</html>