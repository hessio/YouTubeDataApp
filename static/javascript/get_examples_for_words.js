function postData(input) {
	$.ajax({
        	type: "GET",
        	url: "/"+input,
        	success: callbackFunc
            });
        }

        function callbackFunc(response) {
          
          var foo = document.getElementById("sconce");
          foo.innerHTML = "";
          const regex = /\"\d+\"\:/;
          var videos = response;
          var stringss = videos.split(regex)
          stringss.shift();
          
          var arr = [];
          while(arr.length < 8){
              var r = Math.floor(Math.random() * stringss.length) + 1;
              if(arr.indexOf(r) === -1) arr.push(r);
          }

          var foo = document.getElementById("sconce");
          let video_heading = document.createElement('h3');
          video_heading.innerHTML += '<h2>Click any video to watch in a new tab</h2>';
          foo.appendChild(video_heading);

          var all_v = '';
          const regex_im_url = /https:\/\/i.ytimg.com\/vi\/[-\w]+\/[a-z]*default.jpg/
          const regex_video_url = /https:\/\/www.youtube.com\/watch\?v=[-\w]+/

          for (let i = 0; i < arr.length; i++) {
            im_url = stringss[arr[i]].match(regex_im_url);
            video_url = stringss[arr[i]].match(regex_video_url);
            
            new_str = stringss[arr[i]].split(regex_im_url)[1];
            new_str = new_str.slice(4, -5);

            let createNewDiv = document.createElement('div');
            var foo = document.getElementById("sconce");
            createNewDiv.className = 'example';
            createNewDiv.innerHTML += '<a href="'+video_url+'" target="_blank"><img src="' +im_url + '" id="picture"><p class="title">'+new_str+'</p></a>'
            foo.appendChild(createNewDiv);
	}
}

