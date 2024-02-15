//object to store questions and if they are answered true or false
let questions = {};
let num_of_questions = 0;

let buttonCounter = 0;
const submitBtn = document.getElementById("submit-btn");
const questionTitle = document.getElementById("question");

//to store array of 1s and 0s (true and false answers to questions) to be sent for processing
const answers = [];


window.onload = event => {
    //get questions from csv  
    fetch("/data")
    .then(response => response.json())
    .then(response => {
        console.log("Data!");
        console.log(response.data);
        question_names = response.data;

        //add each question to "questions" object with "answered" value set to 0
        question_names.forEach((elem, index) => {
            questions[elem] = 0;
        })

        console.log(JSON.stringify(questions, null, 4));

        //the total number of questions, based on incoming csv data
        num_of_questions = question_names.length;
        //randomly order questions for asking user
        shuffleQuestions(question_names);
        //display first question
        document.getElementById("question").innerHTML = question_names[0];
    })
    .catch(error => console.log(error));
}


//understand this fully later
function shuffleQuestions(qList) {
    for (let i = qList.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        let temp = qList[i];
        qList[i] = qList[j];
        qList[j] = temp;
    }
}

//submit button only displays after certain number of true/false clicks (currently 5 for testing, will be 20)
function trueClick(){
    //get current question name and find it in object, change "answered" value to 1 for respective question
    current_qname = question_names[buttonCounter];
    questions[current_qname] = 1;
    buttonCounter++;
    if(buttonCounter >= num_of_questions){ //if max is reached, disable both buttons and display the submit button
        document.getElementById("true-btn").disabled = true;
        document.getElementById("false-btn").disabled = true;
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = question_names[buttonCounter]; //next question in array is displayed
    }
}

function falseClick(){
    // answers.push(0); //add 0 for false answers
    buttonCounter++;
    if(buttonCounter >= num_of_questions){ //if max is reached, disable both buttons and display the submit button
        document.getElementById("true-btn").disabled = true;
        document.getElementById("false-btn").disabled = true;
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = question_names[buttonCounter]; //next question in array is displayed
    }
}

function submitClick(){
    console.log(JSON.stringify(questions, null, 4));

    for(let x in questions) {
        answers.push(questions[x]);
    }
    console.log(answers);

    // fetch('/process') //get data from flask app route that handles the process route
    // .then(response => response.text())
    // .then(text => {
    //     console.log('GET Request')
    //     console.log(text);
    // })

    fetch('/process', {

        //declare what type of content we are sending
        headers: {
            'Content-type': 'application/json' 
        },

        //specify HTTP method
        method: 'POST',

        //JSON to be sent
        body: JSON.stringify({
            "answers": answers
        })
    }).then(response => response.json())
    .then(data => {
        console.log(data)

        let num_of_true_answers = data.total;
        document.getElementById("true-num").innerHTML = num_of_true_answers;

        document.getElementById("results-container").style.display = 'block';
    })
    .catch(error => console.log(error))
}

function correctAnswer(){
    document.getElementById("verify-answer").style.display = "none";
    document.getElementById("next-steps-true").style.display = "block";
}

function wrongAnswer(){
    document.getElementById("verify-answer").style.display = "none";
    document.getElementById("next-steps-false").style.display = "block";
}