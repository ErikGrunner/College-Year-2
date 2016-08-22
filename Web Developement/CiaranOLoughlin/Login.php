<!DOCTYPE html>
<!--Login php file to process login from user-->
<html>
<body>
<?php
	echo "<br>";
	echo "<br>";
	echo "<br>";
	echo "<br>";
	echo $_GET["User_name"];
	echo "<br>";
	echo "<br>";
	echo "<br>";
	$con=mysqli_connect("localhost","root","","dt211_2_webd");
	if(!$con)
	{
		echo ("Failed to connect to MYSQL:".mysqli_connect_errno());
	}
	
	else
	{
		echo "Connected";
	}
	echo "<br>";
	
	$name=$_GET["User_name"];
	$pass=$_GET["password"];
	//get usernames and passwords
	$sql = "SELECT UserName,FirstName,LastName,Password FROM user";
	$result = $con->query($sql);
	
	if ($result->num_rows > 0) {
    // output data of each row
		while($row = $result->fetch_assoc()) {
			if($name==$row["UserName"] && $pass==$row["Password"])//if the username and password match redirect the user to home page
			{
				header('Location: Home.html');
				
			}
			Else
			{
				header('Location: Login.html');//otherwise send them back to login page
				exit;
			}
		}
	}
$con->close();
?>
</body>
</html>