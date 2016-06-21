function vgWortPixelCall(publicCode, server) {
	if (server === undefined) {
		server = "http://vg08.met.vgwort.de/na";
	}
	var img = document.createElement("IMG");
	img.src = server+"/"+publicCode;
	img.width = 1;
	img.height = 1;
	document.getElementById("vgwpixel").appendChild(img); 
}