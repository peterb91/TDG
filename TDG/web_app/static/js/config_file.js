if (window.File && window.FileReader && window.FileList && window.Blob) {
// Check if browser supports File API and FileReader features
  $(document).ready(function () {
    document.getElementById("export_btn").onclick = function() {
	// Handling data provided by User and export them to config file
	
	    var data = $( ":input" ).serializeArray(); // Assign all input data as a array to variable 
		var txtContent = "";
		$(data).each(function(index, field) {
		    dataString = field.name + " = " + field.value;
			txtContent += index < (data.length - 1) ? dataString + "\r\n" : dataString;
			}); // Generating "name = value" string from inputs provided by User
		
		function download(content, fileName, mimeType) {
		// Creating download function which takes txt string, the filename and mimeType as parameters
		    
			var a = document.createElement('a');
			var blob = new Blob([content], { type: mimeType}); // Creating Blob, a file-like object of immutable, raw data
			var mimeType = mimeType || "application/octet-stream";
			
			if (URL && "download" in a) { 
			    a.href = URL.createObjectURL(blob); // Creates URL object from a blob file to enable its downloading
				a.setAttribute('download', fileName);
				document.body.appendChild(a);
				a.click();
				document.body.removeChild(a);
			} else {
				location.href = 'data:application/octet-stream,' + encodeURIComponent(content);
			}
	    }
	    download(txtContent, "config_file.txt", "text/csv;encoding:utf-8");
	}
  });

  $(document).ready(function () {
    document.getElementById("import_btn").onchange = function(event) {
	// Parsing data from imported config ile and filling in them in form
    
		var file = event.target.files[0]; // Retrieve the first (and only) File from the FileList object
		var reader = new FileReader(); // Generate a new FileReader object
		var data = "";
		
		reader.onload = function() {
		    var text = this.result; // Assign the file/blob's text string data to variable
			var lines = text.split(/\r\n|\n/);
			lines = lines.filter(function(record) {
			    return record !== "";
				});
				
			var keyValueString = lines.map((line) => {
			    var arr = line.split("=").map((item) => {
				    return item.trim();
					});
				arr = `${JSON.stringify(arr[0])}: ${JSON.stringify(arr[1])}`;
				return arr;
			});
			
			data = `{${keyValueString}}`;
			var dataObj = JSON.parse(data); // Parsing string data into JavaScript object
			// Inserting values from the file to appropriate inputs of the form
			$("[name=records_no]").val(dataObj.records_no);
			$("[name=ratio]").val(dataObj.ratio);
			$("#" + dataObj.headers).attr("checked", true);
			$("[name=login_min_length]").val(dataObj.login_min_length);
			$("[name=login_max_length]").val(dataObj.login_max_length);
			$("#" + dataObj.login_special_char).click();
			$("[name=login_textarea_custom]").val(dataObj.login_textarea_custom);
			$("[name=pass_min_length]").val(dataObj.pass_min_length);
			$("[name=pass_max_length]").val(dataObj.pass_max_length);
			$("#" + dataObj.pass_special_char).click();
			$("[name=pass_textarea_custom]").val(dataObj.pass_textarea_custom);
        };

		reader.onerror = function() {
		    alert(event.target.error.name);
		};
		reader.readAsText(file); // Reading file as a text string decoded by default as 'UTF-8'
	};
  });
} else {
    alert('The File APIs are not fully supported in this browser.');
}