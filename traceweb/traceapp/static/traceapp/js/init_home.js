
var processing = false;
// When the form is submitted
$("#itemreg_submit").click(function(){ 
// -- Start AJAX Call --
 if(processing) {
        return;
    }
processing = true;
$.ajax({ 
    url: 'http://localhost:8000/regItem',  // Send the login info to this page
	data: {itemName: itemreg_form.elements["name"].value, itemID: itemreg_form.elements["item_id"].value },
    success: function(data){
		processing = false;
		if(data=="valid"){
			alert("Added item!");
		}else if(data=="invalid"){
			alert("Could not add item, try again.");
		}
	},
    failure: function(data){
		alert('Got an error');
	}
  }); 
   
// -- End AJAX Call --
 
return false;
 
}); // end submit event
 

