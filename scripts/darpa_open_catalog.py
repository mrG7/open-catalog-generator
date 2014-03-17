#!/usr/bin/python
import time
def logo(office):
  logo= "<div style='background:black;'><a href='http://www.darpa.mil/'><img class='darpa-logo' src='darpa-transparent-v2.png'></a><span style='line-height:60px;'><h2 class='darpa-header'><a href='index.html' class='topheaderlink'>Open Catalog</a>"
  if (office != ""):
    logo += "<font color='white'> / %s </font></h2>" % office
  logo += "</span></div>"
  return logo

def catalog_splash_content():
  date = time.strftime("%Y-%m-%d", time.localtime())
  splash = """
<br><p>Welcome to the DARPA Open Catalog, which contains a curated list of DARPA-sponsored software and peer-reviewed publications. DARPA sponsors fundamental and applied research in a variety of areas including data science, cyber, anomaly detection, etc., which may lead to experimental results and reusable technology designed to benefit multiple government domains.</p>
<p>The DARPA Open Catalog organizes publically releasable material from DARPA programs. DARPA has an open strategy to help increase the impact of government investments.</p>
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
  header = "<table id='software' class='tablesorter'>\n <thead>\n <tr>"
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

$(document).ready(function() 
    { 
        $('#software').tablesorter({
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
		
		//create table tabs
		$(function() {
			$( "#tabs" ).tabs();
		});

		//get the list of tabs and the number of tabs
		var tabList = $('#tabs >ul >li');
		var tabCount = $('#tabs >ul >li').size();

		//configure table search and clear button for software and publications table
		for (var i=0; i<tabCount; i++){

			var tabName = tabList[i].textContent.toLowerCase(); //name of tab
			var tabTable = document.getElementById("tabs" + i).getElementsByTagName('table'); //table within this tab
			var headerRow = tabTable[0].tHead.rows[0].cells; //header row of table
			var tabHeaders = createList = [];

			for (var j=0; j<headerRow.length; j++) 
				tabHeaders.push(headerRow[j].textContent.toLowerCase());	
			
			if(tabName == "software"){
			
				var sw_options = {
				  valueNames: tabHeaders
				};
				
				var swList = new List(tabName, sw_options);
				createList.push(swList);
				
				$("#clear" + i).click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					swList.search();
				});
			}
			
			if(tabName == "publications"){
				
				var pub_options = {
				  valueNames: tabHeaders
				};

				var pubList = new List(tabName, pub_options);
				createList.push(pubList);

				$("#clear" + i).click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					pubList.search();
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

</script>
"""

def catalog_page_footer():
  return """
<div class='footer'><br><br>
<hr>
<p><a href='http://www.darpa.mil/FOIA.aspx'>FOIA</a> | <a href='http://www.darpa.mil/Privacy_Security_Notice.aspx'>Privacy and Security</a> | 
<a href='http://www.darpa.mil/NoFearAct.aspx'>No Fear Act</a> | <a href='http://www.darpa.mil/External_Link.aspx?url=http://dodcio.defense.gov/DoDSection508/Std_Stmt.aspx'>Accessibility/Section 508</a></p>
</div>
</html>
"""
