let buttonCounter = 0;
const submitBtn = document.getElementById("submit-btn");

//submit button only displays after certain number of true/false clicks (currently 5 for testing, will be 20)
function trueClick(){
    buttonCounter++;
    console.log(buttonCounter);
    if(buttonCounter >= 5){
        submitBtn.style.display = "inline-block";
    }
}

function falseClick(){
    buttonCounter++;
    console.log(buttonCounter);
    if(buttonCounter >= 5){
        submitBtn.style.display = "inline-block";
    }
}


