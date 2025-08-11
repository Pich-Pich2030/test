$sql="select username,password from level6_users where id=1";
$result=mysql_query($sql) or die('<pre>'.mysql_error().'</pre>');
$row=mysql_fetch_row($result);
$username=$row1[1];
$sql2="select username,email from level6_users where username="."'".$username."'"
