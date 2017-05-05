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
	let request = createRequest();
	request.open("GET",url,true);
	request.onreadystatechange = function(){
		if (request.readyState == 4){
		if (request.status == 200){
			let response = request.responseText;
			//var response = request.responseXML;
					if (func != false){
						func(response);
					}
				} else {
					alert("Error! Request status is " + request.status);
				}
			}   
		} 
	//request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	//request.setRequestHeader("Content-Type","text/xml");
	request.setRequestHeader("Content-Type","application/json");
	request.send(data);
    }

function postRequest(url,data,func) {
 	// body...
 	let request = createRequest();
	request.open("POST",url,true);
	request.onreadystatechange = function(){
		if (request.readyState == 4){
		if (request.status == 200){
			//var response = request.responseXML;
			let response = request.responseText;
					if (func != false){
						func(response);
					}
				} else {
					alert("Error! Request status is " + request.status);
				}
			}   
		} 
	//request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	//request.setRequestHeader("Content-Type","text/xml");
	request.setRequestHeader("Content-Type","application/json");
	requset.send(data);
 }

