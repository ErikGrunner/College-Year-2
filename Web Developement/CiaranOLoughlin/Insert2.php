<!DOCTYPE html>
<!--Second insert statement to insert into prescription_info table-->
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
			$name=$_GET["name"];
			$cus_add=$_GET["cus_add"];
			$dname=$_GET["dname"];
			$d_add=$_GET["d_add"];
			$d_type=$_GET["d_type"];
			$d_d=$_GET["d_d"];
			$days=$_GET["days"];
			$m_num=$_GET["m_num"];
			$p_num=$_GET["p_num"];
			
			$sql = "INSERT INTO prescription_info (Name_cus,Address_cus, D_name, D_address, Drug_type ,Drug_dosage, Days,M_number,Prescription_num)
			VALUES ('$name','$cus_add','$dname','$d_add','$d_type','$d_d','$days','$m_num','$p_num')";//inserts imputed values to the table prescription_info

			if ($con->query($sql) === TRUE) {
				echo "New record created successfully";
			} else {
				echo "Error: " . $sql . "<br>" . $con->error;
			}

			$con->close();
	?>
	</body>
</html>