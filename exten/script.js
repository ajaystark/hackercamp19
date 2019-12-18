function toOpen(){	
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
		var activeTab = tabs[0];
		var url = activeTab.url;
		dom = url.split('//')[1];
		dom = dom.split('/')[0];
		alert(dom);
	});	
}


behav = $.get('http:/localhost:5000/getProds');

html = '';

for(let i = 0; i < behav.length; i++){
	html += '<div class="rec">'
	html += '<div class="rec-img" style="background-image: url('i1.jpg')"></div>'
	html += '<h3 class="rec-name">'+behav[i][0]+'</h3>'
	html += '<a href="'+behav[i][1]+'"></a>'
	html += '<br>'
	html += '<div class="rating">'+behav[i][2]+'</div>';
	html += '</div>';
}

window.innerHTML += html;