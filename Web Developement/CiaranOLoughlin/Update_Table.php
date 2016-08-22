<!DOCTYPE html>
<!--Update php file to update contents of prescription_info-->
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
			$where=$_GET["where"];
			//update statement in sql with all parametere but table name filled out by user
			$sql = "UPDATE prescription_info SET Name_cus='$name',Address_cus='$cus_add'
			,D_name='$dname',D_address='$d_add',Drug_type='$d_type',Drug_dosage='$d_d'
			,Days='$days' ,M_number='$m_num',Prescription_num='$p_num' WHERE Name_cus='$where'";

			if ($con->query($sql) === TRUE) //error checking
			{
				echo "Record updated successfully";
			} 
			else 
			{
				echo "Error updating record: " . $con->error;
			}
			
			$con->close();
	?>
	</body>
</html>