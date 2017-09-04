var fr; // Variable to store the file reader
var is_img_ready = false;

//Function to load the image from local path to img and canvas 
function loadImage() {
    img_src = document.getElementById('img_src');
    if(!img_src.files[0]) {
        alert('Please select an Image first!')
        return;
    }
    fr = new FileReader();
    fr.onload = updateImage;
    fr.readAsDataURL(img_src.files[0])
}

function updateImage() {
    img = new Image();

    img.onload = function() {
        var canvas = document.getElementById("local_canvas")
        canvas.width = img.width;
        canvas.height = img.height;
        var ctx = canvas.getContext("2d");
        ctx.drawImage(img,0,0);
        //alert(canvas.toDataURL("image/png"));
    };
    img.src = fr.result;
    is_img_ready = true;
}

function loadProcessedImage(data) {
    img = new Image();

    img.onload = function() {
        var processedCanvas = document.getElementById('processed_canvas');
        var localCanvas = document.getElementById('local_canvas');
        processedCanvas.width = localCanvas.width;
        processedCanvas.height = localCanvas.height;
        ctx = processedCanvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
    };
    console.log(data); 
    img.src = 'data:image/jpeg;base64,' + data;
}

function processImage() {
    if (is_img_ready == false) {
        alert('No image to process!');
        return;
    }

    //Send the image to the server and wait for a response
    canvas = document.getElementById('local_canvas');
    image_data = canvas.toDataURL('image/jpeg');
    img_op = document.getElementById('image_op');
    op = img_op.options[img_op.selectedIndex].value;

    $.ajax({
        url:"http://localhost:5000/process_image",
        method: "POST",
        contentType: 'application/json',
        crossDomain: true,
        data: JSON.stringify({
            image_data: image_data,
            msg: 'This is image data',
            operation: op
        }),
        success: function(data){
            loadProcessedImage(data);
        },
        error: function(err) {
            console.log(err)
        }
    });
}
