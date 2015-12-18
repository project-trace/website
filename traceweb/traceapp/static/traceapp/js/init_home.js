
var processing = false;
// When the form is submitted
$("#itemreg_submit").click(function(){ 
// -- Start AJAX Call --
 if(processing) {
        return;
    }
processing = true;
var img = "";
if(document.getElementById('cellphone').checked){
	img = "static/traceapp/img/cellphone.png"
}else if(document.getElementById('wallet').checked){
	img = "static/traceapp/img/wallet.png"
}else if(document.getElementById('keys').checked){
	img = "static/traceapp/img/keys.png"
}else if(document.getElementById('laptop').checked){
	img = "static/traceapp/img/laptop.png"
}else if(document.getElementById('bag').checked){
	img = "static/traceapp/img/bag.png"
}else if(document.getElementById('other').checked){
	img = "static/traceapp/img/item.png"
}
$.ajax({ 
    url: 'http://localhost:8000/regItem',  // Send the info to this page
	data: {itemName: itemreg_form.elements["name"].value, itemDes: itemreg_form.elements["des"].value, itemImg: img},
    success: function(data){
		processing = false;
		if(data=="valid"){
			alert("Added item!");
			location.reload();
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



