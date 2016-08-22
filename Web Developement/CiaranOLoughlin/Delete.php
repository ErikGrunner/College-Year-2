<!DOCTYPE html>
<!--Php file to delete a row from prescription_info-->
<html>
<body>

	<div>
		<b>
		<a  href="Home.html" style="color:Black; position: absolute; left: 600px; margin-top: 1px;font-size: 20px;"> WebD/Assignment</a>
		</b>
	</div>
	
	<div style="position: absolute; left: 10px; margin-top: 25px;width:1350px; height:30px;border:1px solid #000;">
		<A href="view_table.html" style="position: absolute; left: 10px; margin-top: 6px; text-decoration: none;color:Black;">
		Display Table
		</A>
		
	</div>
	
	<div>
		<A href="Insert.html" style="position: absolute; left: 130px; margin-top: 32px; text-decoration: none;color:Black;">
		Insert to a table
		</A>
		
	</div>
	
	<div>
		<A href="Update_Table.html" style="position: absolute; left: 250px; margin-top: 32px; text-decoration: none; color:Black;">
		Update a table
		</A>
	</div>
	<div>
		<A href="Delete.html" style="position: absolute; left: 370px; margin-top: 32px; text-decoration: none; color:Black;">
		Delete table
		</A>
		
	</div>


	<?php
		$con=mysqli_connect("localhost","root","","dt211_2_webd");
		echo "<br>";
		echo "<br>";
		echo "<br>";
		echo "<br>";
			if(!$con)
			{
				echo ("Failed to connect to MYSQL:".mysqli_connect_errno());
			}
			
			else
			{
				echo "Connected";
			}
			echo "<br>";
			$name=$_GET["delete"];
			
			$sql = "DELETE FROM prescription_info WHERE Name_cus= '$name'";//delete request where the name entered by the user= the name of customer in database

			if ($con->query($sql) === TRUE) {
				echo "Delete successful";
			} else {
				echo "Error: " . $sql . "<br>" . $con->error;
			}

			$con->close();
	?>
	</body>
</html>