// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("Read_More_btn");

// Get the <span> element that closes the modal
var span = document.querySelector(".close")

// When the user clicks the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    console.log('clicked');
    modal.style.display = "none";
}


// When the user clicks on <span> (x), close the modal




// Get the modal
var modal_2 = document.getElementById('myModal_2');

// Get the button that opens the modal
var btn_2 = document.getElementById("Read_More_btn_2");

// Get the <span> element that closes the modal
var span_2 = document.getElementsByClassName("close_2")[0];

// When the user clicks the button, open the modal 
btn_2.onclick = function() {
    modal_2.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span_2.onclick = function() {
    console.log('clicked');
    modal_2.style.display = "none";
}


// Get the modal
var modal_3 = document.getElementById('myModal_3');

// Get the button that opens the modal
var btn_3 = document.getElementById("Read_More_btn_3");

// Get the <span> element that closes the modal
var span_3 = document.getElementsByClassName("close_3")[0];


// When the user clicks the button, open the modal 
btn_3.onclick = function() {
    modal_3.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span_3.onclick = function() {
    modal_3.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal_3) {
        modal_3.style.display = "none";
    }
    if (event.target == modal_2) {
        modal_2.style.display = "none";
    }
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


// // Get the modal
// var modal_4 = document.getElementById('myModal_4');

// // Get the button that opens the modal
// var btn_4 = document.getElementById("Read_More_btn_4");

// // Get the <span> element that closes the modal
// var span_4 = document.getElementsByClassName("close_4")[0];

// // When the user clicks the button, open the modal 
// btn_4.onclick = function() {
//     modal_4.style.display = "block";
// }

// // When the user clicks on <span> (x), close the modal
// span_4.onclick = function() {
//     modal_4.style.display = "none";
// }

// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }


// // Get the modal
// var modal_5 = document.getElementById('myModal_5');

// // Get the button that opens the modal
// var btn_5 = document.getElementById("Read_More_btn_5");

// // Get the <span> element that closes the modal
// var span_5 = document.getElementsByClassName("close_5")[0];

// // When the user clicks the button, open the modal 
// btn_5.onclick = function() {
//     modal_5.style.display = "block";
// }

// // When the user clicks on <span> (x), close the modal
// span_5.onclick = function() {
//     modal_5.style.display = "none";
// }

// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }