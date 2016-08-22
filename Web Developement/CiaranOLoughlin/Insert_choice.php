<!DOCTYPE html>
<!--Choic program which just determines which table the user selected and redirects them to the correct page-->
<html>
	<body>

	<?php
		$choice=$_GET["choice"];
		if ($choice=="Pharmacy")//if statement to decide what table the user selected 
		{
			header('Location: Choice.html');
		}
		elseif ($choice=="Prescription")
		{
			header('Location: Choice2.html');
		}
		else
		{
			header('Location: Insert.html');
		}
	?>
	</body>
</html>