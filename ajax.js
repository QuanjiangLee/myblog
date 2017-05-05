function createRequest(){
var request = null;
try {
	request = new XMLHttpRequest();	
} catch (trymicrosoft) {
	try {
		request = new ActiveXObject("Msxm12.XMLHTTP");
	} catch (othermicrosoft) {
		try {
			request = new ActiveXObject("Microsoft.XMLHTTP");
		} catch (failed) {
			request = null;
		}
	}
}

if (request == null){
	alert("Error creating request object!");
} else {
    return request;
    }
}


function getRequest(url,data,func){
   // request.onreadystatechange = 
	var request = createRequest();
	request.open("GET",url,true);
	request.onreadystatechange = function(){
		if (request.readyState == 4){
		if (request.status == 200){
			var response = request.responseText;
			func(response);
				} else {
					alert("Error! Request status is " + request.status);
				}
			}   
		} 
	request.send(data);
    }

function postRequest(url,data,func) {
 	// body...
 	var request = createRequest();
	request.open("POST",url,true);
	request.onreadystatechange = function(){
		if (request.readyState == 4){
		if (request.status == 200){
			var response = request.responseText;
			func(response);
				} else {
					alert("Error! Request status is " + request.status);
				}
			}   
		} 
	//request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	request.setRequestHeader("Content-Type","application/");
	requset.send(data);
 }

function actRequest(argument) {
	// body...
	if (request.readyState == 4){
		if (request.status == 200){
			var response = request.responseText;
		}
	}   
}
