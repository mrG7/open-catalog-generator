#!/usr/bin/python
import time
import getpass

def logo(office):
  logo= "<div class='darpa-header'><a href='http://www.darpa.mil/'><img class='darpa-logo' src='darpa-transparent-v2.png'></a><h2><a href='index.html' class='programlink'><img class='catalog-logo' src='Open-Catalog-Single-Big.png'></a>"
  if (office != ""):
    logo += "<span><font color='white'> / </font> %s </span></h2>" % office
  logo += "</div>"
  return logo

def get_current_user():
  return getpass.getuser()
    
def catalog_splash_content():
  date = time.strftime("%Y-%m-%d", time.localtime())
  splash = """
<p>Welcome to the DARPA Open Catalog, which contains a curated list of DARPA-sponsored software and peer-reviewed publications. DARPA sponsors fundamental and applied research in a variety of areas including data science, cyber, anomaly detection, etc., which may lead to experimental results and reusable technology designed to benefit multiple government domains.</p>
<p>The DARPA Open Catalog organizes publicly releasable material from DARPA programs. DARPA has an open strategy to help increase the impact of government investments.</p>
<p>DARPA is interested in building communities around government-funded software and research. If the R&D community shows sufficient interest, DARPA will continue to make available information generated by DARPA programs, including software, publications, data, and experimental results.</p>
<p>The table on this page lists the programs currently participating in the catalog.</p>
<p>Program Manager:<br>
Dr. Christopher White<br>
<a href='mailto:christopher.white@darpa.mil'>christopher.white@darpa.mil</a></p>
<p>Report a problem: <a href="mailto:opencatalog@darpa.mil">opencatalog@darpa.mil</a></p>
<p>Last updated: """ 
  splash += date + "</p>"
  return splash
  
def splash_table_header():
  return """
<h2>Current Catalog Programs:</h2>
<table id='splash' class='tablesorter'> 
<thead> 
<tr> 
    <th>DARPA Program</th> 
    <th>Description</th> 
</tr> 
</thead> 
<tbody> 
"""

def splash_table_footer():
  return """
</tbody> 
</table>
<br>
"""

def software_table_header(columns):
  header = "<table id='sftwr' class='tablesorter'>\n <thead>\n <tr>"
  for column in columns:
    header += "<th>%s</th>" % column
  header += "</tr>\n </thead>\n <tbody  class='list'>"
  return header

def software_table_footer():
  return """
</tbody> 
</table>
"""

def pubs_table_header():
  return """
<table id='pubs' class='tablesorter'> 
<thead> 
<tr> 
    <th>Team</th> 
    <th>Title</th> 
    <th>Link</th>
</tr> 
</thead> 
<tbody  class="list"> 
"""

def pubs_table_footer():
  return """
</tbody> 
</table>
<br>
"""
  
def catalog_page_header(): 
  return """ 
<html>
<link rel='stylesheet' href='style.css' type='text/css'/>
<link rel='stylesheet' href='banner_style.css' type='text/css'/>
<link rel='stylesheet' href='css/flick/jquery-ui-1.10.4.custom.css' type='text/css'/>
<link rel='stylesheet' href='css/list_style.css' type='text/css'/>

<script type='text/javascript' src="list.min.js"></script>
<script type='text/javascript' src='jquery-latest.js'></script>
<script type='text/javascript' src="jquery-1.9.1.js"></script>
<script type='text/javascript' src="jquery-ui.js"></script>
<script type='text/javascript' src='jquery.tablesorter.min.js'></script>


<script type='text/javascript'>
var swList = pubList = spubList = ssftList = "";

$(document).ready(function() 
    { 
        $('#sftwr').tablesorter({
		// sort on the first column and second column, order asc 
        	sortList: [[0,0],[1,0]] 
    	}); 
        $('#pubs').tablesorter({
        	sortList: [[0,0],[1,0]] 
    	});
        $('#splash').tablesorter({
		// sort on the first column, order asc 
        	sortList: [[0,0]] 
    	});
		
		//get the list of tabs and the number of tabs
		var tabList = $('#tabs >ul >li');
		var tabCount = $('#tabs >ul >li').size();

		
		//create table tabs

		$(function() {
			$( "#tabs" ).tabs();
			if($("#tabs0"))
				$("#tabs").tabs({active: 0});  //software tab
			else
				$("#tabs").tabs({active: 1});  //publications tab
		});

		//configure table search and clear button for software and publications table
		for (var i=0; i<tabCount; i++){
			
			var tabName = tabList[i].textContent.toLowerCase(); //name of tab

			if(tabName == "software"){
				var tabTable = $('#tabs0 table'); //table within this tab
				var tabHeaders = getTableHeaders(tabTable);	
				
				var sw_options = {
				  valueNames: tabHeaders
				};
				
				swList = new List(tabName, sw_options);

				$("#clear0").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					swList.search();
				});
			}
			
			if(tabName == "publications"){
				var tabTable = $('#tabs1 table'); //table within this tab
				var tabHeaders = getTableHeaders(tabTable);	
				
				var pub_options = {
				  valueNames: tabHeaders
				};

				pubList = new List(tabName, pub_options);

				$("#clear1").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					pubList.search();
				});
				
			}
			
			if(tabName == "search"){

				var table_clone = $('#tabs table').clone();
				for (var k=0; k<table_clone.length; k++){
					var searchHeaders = getTableHeaders(table_clone[k]);
					var search_options = {
						  valueNames: searchHeaders
					};
					
					if (table_clone[k].id == "sftwr"){
						$("#softwareSearch #sftwrTable").append(table_clone[k]);
						//tables are hidden initially
						$("#softwareSearch #sftwrTable").hide();
						ssftList = new List("softwareSearch", search_options);					
					}
					else{
						$("#publicationsSearch #pubTable").append(table_clone[k]);
						$("#publicationsSearch #pubTable").hide();
						spubList = new List("publicationsSearch", search_options);
					}
					
				}

				$("#clear2").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					if (ssftList != "")
						ssftList.search();
					if (spubList != "")
						spubList.search();
					//when search is cleared tables need to be hidden
					$("#softwareSearch #sftwrTable").hide();
					$("#publicationsSearch #pubTable").hide();
						
				});

			}
		}   
    } 
);

function jump(h){
    var url = location.href;
    location.href = "#"+h;
        history.replaceState(null,null,url)
}

function pubSearch(link){
	var search_text = link.hash.replace("#", "");
	$('#tabs').tabs({active: 1}); //publications tab
	var search_box = $("#search1");
	search_box.val(search_text);

	setTimeout(function(){
		search_box.focus();
		search_box.select();
		pubList.search(search_text); 
	},300);
}

function allSearch(this_search){
	if(this_search.value != "" && this_search.value.length >= 3){
		var value = this_search.value; 
		//TODO: Implement Stop Words
		ssftList.search(value);
		
		//hide table if there are no rows that match the search term
		if ($("#softwareSearch #sftwrTable tbody").children().length != 0)
			$("#softwareSearch #sftwrTable").show();
		else
			$("#softwareSearch #sftwrTable").hide();
		
		if(spubList != ""){
			var value = this_search.value;
			spubList.search(value);
			
			if ($("#publicationsSearch #pubTable tbody").children().length != 0)
				$("#publicationsSearch #pubTable").show();
			else
				$("#publicationsSearch #pubTable").hide();
		}
	}
	else{
		//if search_term is empty or not 3 chars in length, make sure the tables are hidden
		$("#publicationsSearch #pubTable").hide();
		$("#softwareSearch #sftwrTable").hide();
	}
}

function getTableHeaders(table){
	var this_table;
	 
	if(table[0])
		this_table = table[0];
	else
		this_table = table;
		
	var headerRow = this_table.tHead.rows[0].cells; //header row of table
	var tableHeaders = [];

	for (var j=0; j<headerRow.length; j++) 
		tableHeaders.push(headerRow[j].textContent.toLowerCase());

	return tableHeaders;		
}

function licenseInfo(table_data, license_content, license_nm){

	for (content in license_content){
		if(license_nm.trim() == license_content[content]['License Short Name'] || license_nm.trim() == license_content[content]['License Long Name']){
			
			if(license_content[content]['License Short Name'] != ""){
				$( "#dialog" ).empty().dialog({
						position: { my: "left", at: "bottom+500%", of: table_data },
						title: license_content[content]['License Short Name'],
						
				});
				
				if(license_content[content]['License Description'] != "")
					$("#dialog").html("<a href='" + license_content[content]['License Link'] + "'>" + license_content[content]['License Long Name'] + "</a>: " + license_content[content]['License Description']);
				else
					$("#dialog").html("<a href='" + license_content[content]['License Link'] + "'>" + license_content[content]['License Long Name'] + "</a>");
			}
			
			break;
		}
	}
	
}
</script>
"""

def catalog_page_footer():
  return """
<div class='footer'>
<hr>
<p><a href='http://www.darpa.mil/FOIA.aspx'>FOIA</a> | <a href='http://www.darpa.mil/Privacy_Security_Notice.aspx'>Privacy and Security</a> | 
<a href='http://www.darpa.mil/NoFearAct.aspx'>No Fear Act</a> | <a href='http://www.darpa.mil/External_Link.aspx?url=http://dodcio.defense.gov/DoDSection508/Std_Stmt.aspx'>Accessibility/Section 508</a></p>
</div>
</html>
"""
