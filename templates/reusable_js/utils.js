
function getPrograms() {
	var programs;
	$.ajax({
		async: false,
		url: 'active_content.json',
		dataType: 'json',
		success: function(response){
		   programs = response;
		}
	});
	return programs;
}

function getProgramDetails(filename) {
	var data;
	$.ajax({
		async: false,
		url: filename,
		dataType: 'json',
		success: function(response){
		   data = response;
		}
	});
	return data;
}

function getLicenses() {
	var licenses;
	$.ajax({
		async: false,
		url: 'license-content.json',
		dataType: 'json',
		success: function(response){
		   licenses = response;
		}
	});
	
	return licenses;
}

function isInArray(value, array) {
  //checks to see if a value exists in an array
  return array.indexOf(value) > -1;
}

function isIE() {
	var ua = window.navigator.userAgent;
	var msie = ua.indexOf("MSIE ");
	//check for ie10 and below or ie. If IE browser, return true. If another browser, return false
	if (msie > 0 || window.navigator.msMaxTouchPoints !== void 0 )    
		return true;
	else    
		return false;
}

function sortByProperty(property) {
	//sorts json array by a given property name
    return function (a, b) {
        var sortStatus = 0;
        if (a[property].toLowerCase().trim() < b[property].toLowerCase().trim())
            sortStatus = -1;
        else if (a[property].toLowerCase().trim() > b[property].toLowerCase().trim())
            sortStatus = 1;
 
        return sortStatus;
    };
}

function sortByMultipleProperties(property1, property2) {

	var property_a = property_b = property1;
    return function (a, b) {

        var sortStatus = 0;
		
		if(typeof(a[property_a]) == "undefined")
			property_a = property2;
		if(typeof(b[property_b]) == "undefined")
			property_b = property2;
		
        if (a[property_a].toLowerCase().trim() < b[property_b].toLowerCase().trim())
            sortStatus = -1;
        else if (a[property_a].toLowerCase().trim() > b[property_b].toLowerCase().trim())
            sortStatus = 1;
 
		property_a = property_b = property1;
        return sortStatus;
    };
}

function getStringArray(object) {
	return object = typeof object == 'string' ? [object] : object;
}

function toCamelCase(str) {
	return str.replace(/(?:^|\s)\w/g, function(match) {
	  return match.toUpperCase();
	});
}

function validEmail(item) {
	
	var value = null;
	
	if(item.value) value = item.value;
	else value = item;
		
	var filter = /(([a-zA-Z0-9\-?\.?]+)@(([a-zA-Z0-9\-_]+\.)+)([a-z]{2,3}))+$/;
	return filter.test(value);
}

function getModificationDate(new_date, update_date){
	var change_date = "", change_text = "";
	var change_set = [];

	
	if(new_date == "" && update_date == ""){
		change_set["Date Type"] = change_text;
		change_set["Date"] = change_date;
	}
	else{
		if (new_date != "" && update_date != ""){
			if (new_date >= update_date){
			 change_date = new_date;
			 change_text = "Created";
			}
			else{
			  change_date = update_date;
			  change_text = "Updated";
			}
		}
		else if( new_date != "" && update_date == ""){
			change_date = new_date;
			change_text = "Created";
		}
		else if(update_date != "" && new_date == ""){
			change_date = update_date;
			change_text = "Updated";
		}
		
		change_set["Date Type"] = change_text;
		change_set["Date"] = change_date;
	}

	return change_set;
}