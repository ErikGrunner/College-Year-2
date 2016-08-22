<!DOCTYPE html>
<!--First insert php file to insert to the table pharmacy-->
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
			$name=$_GET["Drug"];
			$stcode=$_GET["st"];
			$desc=$_GET["desc"];
			$pack=$_GET["Pack"];
			$brand=$_GET["name"];
			$cprice=$_GET["cprice"];
			$rprice=$_GET["rprice"];
			$dtype=$_GET["Dtype"];
			//Assigns the inputed data to variables
			$sql = "INSERT INTO pharmacy (Drug,Stock_code, Description, Pack_size, Brand_name ,Cost_price, Retail_price,Drug_type)
			VALUES ('$name','$stcode','$desc','$pack','$brand','$cprice','$rprice','$dtype')";//Inserts received data into the table pharmacy

			if ($con->query($sql) === TRUE) {
				echo "New record created successfully";
			} else {
				echo "Error: " . $sql . "<br>" . $con->error;
			}

			$con->close();
	?>
	</body>
</html>