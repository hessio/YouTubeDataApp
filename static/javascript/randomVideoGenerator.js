function randomVideoFunction(type) {
      const data = new FormData();
      data.append('sort', type);

      let new_vid = 'https://www.youtube.com/embed/';
      var id = '';
      var request = new XMLHttpRequest();
      
      request.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                  id = this.responseText;
                  new_vid += id;
                  new_vid += '?autoplay=1&muted=1';
                  var iframe = document.getElementById('framed');
                  iframe.src = new_vid;
            }
      };
 
      request.open('POST', '/getRandomID');
      request.send(data);
}