<!DOCTYPE html>
<!--PHP file to process which table to display from viewtable.html-->
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
		//connecting to database dt211_WebD
		$con=mysqli_connect("localhost","root","","dt211_2_webd");
		echo "<br>";
		echo "<br>";
		echo "<br>";
		echo "<br>";
			if(!$con)//error detection
			{
				echo ("Failed to connect to MYSQL:".mysqli_connect_errno());
			}
			
			else
			{
				echo "Connected";
			}
			echo "<br>";
			echo "<br>";
			$name=$_GET["Table"];
			if ($name=="Pharmacy")//if statement to decide what table to open and display
			{
				$sql = "SELECT * FROM pharmacy ";
				$result2 = $con->query($sql);

				if ($result2->num_rows > 0) {
					// output data of each row
					while($row = $result2->fetch_assoc()) {
						echo "Drug: " . $row["Drug"]."<br>";
						echo "Stock code: " . $row["Stock_code"]. "<br>";
						echo "Description: " . $row["Description"]. "<br>";
						echo "Pack Size: " . $row["Pack_size"]."<br>";
						echo "Brand Name: " . $row["Brand_name"]."<br>";
						echo "Cost price: " . $row["Cost_price"]."<br>";
						echo "Retail Price: " . $row["Retail_price"]."<br>";
						echo "Drug type: " . $row["Drug_type"]."<br>";
						echo "<br>";
						echo "<br>";
					}
				}
				 else {
					echo "0 results";
				}
			}
			elseif ($name=="Prescription"){
				$sql = "SELECT * FROM prescription_info ";
				$result2 = $con->query($sql);

				if ($result2->num_rows > 0) {
					// output data of each row
					while($row = $result2->fetch_assoc()) {
						echo "Name: " . $row["Name_cus"]."<br>";
						echo "Address: " . $row["Address_cus"]. "<br>";
						echo "Doctor Name: " . $row["D_name"]. "<br>";
						echo "Doctor Address: " . $row["D_address"]."<br>";
						echo "Drug type: " . $row["Drug_type"]."<br>";
						echo "Drug dosage: " . $row["Drug_dosage"]."<br>";
						echo "Days to be taken: " . $row["Days"]."<br>";
						echo "Medical card number: " . $row["M_number"]."<br>";
						echo "Prescription Number: " . $row["Prescription_num"]."<br>";
						echo "<br>";
						echo "<br>";
					}
				}
				 else {
					echo "0 results";
				}
			}
			elseif ($name=="User"){
				$sql = "SELECT * FROM user ";
				$result2 = $con->query($sql);

				if ($result2->num_rows > 0) {
					// output data of each row
					while($row = $result2->fetch_assoc()) {
						echo "User: " . $row["UserName"]. "<br> Password: " . $row["Password"]. "<br> First Name: " . $row["FirstName"]. "<br> Last Name: " . $row["LastName"]."<br>";
						echo "<br>";
						echo "<br>";
					}
				}
				 else {//error checking
					echo "0 results";
				}
			}
			else{//error checking
				echo "Table does not exist";
			}
		$con->close();
	?>
	</body>
</html>