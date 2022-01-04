var url= "http://127.0.0.1:5000";
//this variable for showing the search's result
var app = new Vue({
    el: "#boddy_result",
    delimiters : ['[[', ']]'],
    data: {
      search_results:[]
    }
  });
  

// show the chosen image in images dev and change its border 
function chooseOne(src){
  var el = document.getElementById("imageShow");
   el.innerHTML="<img class=\"image-upload\" src="+src+">";

  $('img').click(function() {  
    $('img').css("border","none");    
  $(this).css("border","3px solid green");  
   });
    var srcc= "";
    srcc = "./images/"+src.split('/')[4].split('.')[0]+".png";
   document.getElementById("searchONE").value= srcc;
}

function SearchImage(value){
  if(value != ""){ 
    fetch(`${url}/search/${value}`)
       .then(response => response.json())
       .then(response => {
         app.search_results = response.map(x => {
            let result = {};
            Object.assign(result, x);
            console.log(result)
            result.name = result.path.split('/')[1].split('.')[0];
            return result;
                    
          })                
 console.log(app.search_results);
            })
    }
}



// show the uploaded image in dev 
function PreviewImage() {
  var oFReader = new FileReader();
  oFReader.readAsDataURL(document.getElementById("file").files[0]);
  oFReader.onload = function (oFREvent) {
  var el = document.getElementById("imageShow");
  el.innerHTML="<img class=\"image-upload\" src="+oFREvent.target.result+">";
  };  
  };

// change the button rechercher value by uploaded image source 
document.getElementById("upload").click(function() {   
document.getElementById("searchONE").value= document.getElementsByName("imageUploaded").name;
alert(document.getElementsByName("imageUploaded").name);
});


// upload Image
function send() {
  const formData = new FormData();
  const img = document.getElementById("file").files[0];
  formData.append("image", img);
  getName(img.name);
  axios.post('http://localhost:5000/upload-image', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(function (response) {
      console.log(response.data)

  }).catch(function (error) {
      console.log(error);
  });

}


function getName(imgName){
  document.getElementById("searchONE").value="./static/images/searched/"+imgName
}


function SearchImagePertinanceDown(value){
  if(value != ""){ 
    fetch(`${url}/search_pertinance_down/${value}`)
       .then(response => response.json())
       .then(response => {
         app.search_results = response.map(x => {
            let result = {};
            Object.assign(result, x);
            console.log(result)
            result.name = result.path.split('/')[1].split('.')[0];
            return result;
                    
          })                
 console.log(app.search_results);
            })
    }
}


function SearchImagePertinanceUp(value){
  if(value != ""){ 
    fetch(`${url}/search_pertinance_up/${value}`)
       .then(response => response.json())
       .then(response => {
         app.search_results = response.map(x => {
            let result = {};
            Object.assign(result, x);
            console.log(result)
            result.name = result.path.split('/')[1].split('.')[0];
            return result;
                    
          })                
 console.log(app.search_results);
            })
    }
}