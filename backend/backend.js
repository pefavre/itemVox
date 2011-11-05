var express = require('express');

var app = express.createServer(express.logger())

var associations = {'456' : 'contenuDe456'};

// for each box, associates a structure containing data about the box
// fields in box : 
//   - lastEmptyRfid
//   - lastRfid
var boxesData = {}


// gets box <idBox> informations
var getBoxData = function(idBox) {
	var box = boxesData[idBox];
	if (undefined == box) {
		boxesData[idBox] = {};
		box = boxesData[idBox];
	}
	return box;
}


var getContentForTag = function(idTag) {
	return associations[idTag];
}

var setContentForTag = function(idTag, content) {
	associations[idTag] = content;
}


// Returns the content associated with rfid tag <:idTag> 
// :idBox UNUSED. It is not strictly necessary, but may be used to track the actions of a box.
// tests :
//   - http://localhost:3000/getContent/123/456
app.get('/getContent/:idBox/:idTag', function(request, response) {
	var idBox = request.params.idBox;
	var idTag = request.params.idTag;
	var responseData = {};

	console.log('get content for tag ' + idTag + ' (on behalf of box ' + idBox + ')');

	var box = getBoxData(idBox);
	var tagContent = getContentForTag(idTag);

	console.log('box: ' + box);

	box.lastTag = idTag;

	if (undefined == tagContent) {
		console.log('no content associated')
		box.lastEmptyTag = idTag;
	}
	else {
		console.log('content associated : ' + tagContent);
		var r = {};
		responseData[idTag] = tagContent;
		box.lastEmptyTag = undefined;
	}

	response.send(responseData);
});

// gets the last empty rfid seen by box <:idBox>, if no other action has been made by the box in the meantime.
app.get('/lastEmptyRfid/:idBox', function(request, response) {
	var idBox = request.params.idBox;
	var responseData = {};

	var box = getBoxData[idBox];

	lastRfid = box.lastEmptyRfid;
	if (undefined != lastRfid) {
		console.log('box ' + idBox + ' has last rfid: ' + lastRfid);
		responseData[idBox] = lastRfid;
	}
	else {
		console.log('last rfid on box ' + idBox + ' was not empty');
	}
	response.send(responseData);
});


app.get('/setContent/:idBox/:idTag/:uri', function(request, response) {
	var idBox = request.params.idBox;
	var idTag = request.params.idTag;
	var uri = request.params.uri;
	var responseData = {};

	console.log('Will add relation ' + idTag + ' <-> ' + uri + ', (on behalf of box ' + idBox + ')');

	setContentForTag(idTag, uri);
	response.send(responseData);
});


app.get('/getAllAssoc', function(request, response) {
	response.send(associations);
});

app.get('/resetAllAssoc', function(request, response) {
	associations = {};
});

app.get('/resetAllBoxes', function(request, response) {
	boxesData = {};
});


app.listen(3000);
