
var url= "http://127.0.0.1:5000";


function get_random_image(){ 
    fetch(`${url}/allImages`)
    .then(res => res.json())
    .then(data => {
        change_random_image(data);
    });


}
function change_random_image(data){
    
    var image_array=data;


    // Get a random index
    random_index1 = Math.floor(Math.random() * image_array.length);
    random_index2 = Math.floor(Math.random() * image_array.length);
    random_index3 = Math.floor(Math.random() * image_array.length);
    random_index4 = Math.floor(Math.random() * image_array.length);
    random_index5 = Math.floor(Math.random() * image_array.length);
    random_index6 = Math.floor(Math.random() * image_array.length);
    random_index7 = Math.floor(Math.random() * image_array.length);
    random_index8 = Math.floor(Math.random() * image_array.length);
    random_index9 = Math.floor(Math.random() * image_array.length);

    // Get an image at the random_index
    selected_image1 = image_array[random_index1]
    selected_image2 = image_array[random_index2]
    selected_image3 = image_array[random_index3]
    selected_image4 = image_array[random_index4]
    selected_image5 = image_array[random_index5]
    selected_image6 = image_array[random_index6]
    selected_image7 = image_array[random_index7]
    selected_image8 = image_array[random_index8]
    selected_image9 = image_array[random_index9]

    // Display the image
    document.getElementById('image1').src = `./images/${selected_image1}`
    document.getElementById('image2').src = `./images/${selected_image2}`
    document.getElementById('image3').src = `./images/${selected_image3}`
    document.getElementById('image4').src = `./images/${selected_image4}`
    document.getElementById('image5').src = `./images/${selected_image5}`
    document.getElementById('image6').src = `./images/${selected_image6}`
    document.getElementById('image7').src = `./images/${selected_image7}`
    document.getElementById('image8').src = `./images/${selected_image8}`
    document.getElementById('image9').src = `./images/${selected_image9}`


    document.getElementById('image1').alt = `${selected_image1}`
    document.getElementById('image2').alt = `${selected_image2}`
    document.getElementById('image3').alt = `${selected_image3}`
    document.getElementById('image4').alt = `${selected_image4}`
    document.getElementById('image5').alt = `${selected_image5}`
    document.getElementById('image6').alt = `${selected_image6}`
    document.getElementById('image7').alt = `${selected_image7}`
    document.getElementById('image8').alt = `${selected_image8}`
    document.getElementById('image9').alt = `${selected_image9}`

}


