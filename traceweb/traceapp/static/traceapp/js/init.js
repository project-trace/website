
// When DOM is ready
$(document).ready(function(){
 
// Launch MODAL BOX if the Login Link is clicked
$("#login_link").click(function(){
    $('#login_form').modal();
});
$("#reg_link").click(function(){
    $('#reg_form').modal();
});

//close modal
$("#close").click(function(){
    $('#login_form').modal('hide');
});
 
$("#closereg").click(function(){
    $('#reg_form').modal('hide');
});

var processing = false;
// When the form is submitted
$("#status > form").submit(function(){ 
// -- Start AJAX Call --
 if(processing) {
        return;
    }
processing = true;
$.ajax({ 
    url: 'http://localhost:8000/loginUser',  // Send the login info to this page
	data: {username: daform.elements["username"].value, password: daform.elements["password"].value },
    success: function(data){
		if(data=="valid"){
			window.location='http://localhost:8000/' + daform.elements["username"].value
			return false;
		}else if(data=="invalid"){
			alert("Invalid credentials, try again");
			processing = true;
			return false;
		}
		processing = false;
	},
    failure: function(data){
		alert('Got an error');
	}
  }); 
   
// -- End AJAX Call --
 
return false;
 
}); // end submit event
 


var processing_reg = false;
// When the form is submitted
$("#submit_reg").click(function(){ 
// -- Start AJAX Call --
 if(processing_reg) {
        return false;
    }
processing_reg = true;
$.ajax({ 
	beforeSend: function(data){
		processing_reg = true;
	},
    url: 'http://localhost:8000/signUp',  // Send the info to this page
	data: {username: daform_reg.elements["username"].value, password: daform_reg.elements["password"].value, first_name: daform_reg.elements["first_name"].value, last_name: daform_reg.elements["last_name"].value },
    success: function(data){
		if(data=="valid"){
			alert("User was created");
			window.location='http://localhost:8000/';			
		}else if(data=="invalid"){
			alert("User was not created, try again");
		}
	},
    failure: function(data){
		alert('Got an error');
	}
  }); 
   
// -- End AJAX Call --
 
return false;
 
}); // end submit event


});

