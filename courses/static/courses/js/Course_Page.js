var NoOfSemester = 7;
var currentSem = 1;
var all_the_course={1:"",2:"",3:"",4:"",5:"",6:"",7:""};
var Courses = all_the_course[currentSem];
const data = document.currentScript.dataset;
const user_usn = data.usn;

//const from html
const CourseContainer = document.getElementById("CourseContainer");  
const dropdown = document.getElementById("dropdown");  
const useinfo = document.getElementById("useinfo");  

//User Usnz
var span = document.createElement('span');
span.classList.add("user_usn");
span.innerHTML = user_usn;
useinfo.appendChild(span);


//Add Semester option based on No of semester
for (let index = 0; index < NoOfSemester; index++) {

  var a = document.createElement('a');
  a.setAttribute("href","");
  a.innerHTML=`<li>Semester `+(index+1)+`</li>`;
  dropdown.appendChild(a);
}

function log(theElement) {
  let course_name = theElement.srcElement.id;
  sessionStorage.setItem("course", course_name);
  // console.log(sessionStorage.getItem("course"));
  location.assign("/features");
}

//For Every course insert card 
Courses.forEach(Course => {
    //Creted div with class card;
    var div = document.createElement('div');
    div.classList.add("card");
    CourseContainer.appendChild(div);
    //Creted div with class course-preview and make card as parent;
    var div1 = document.createElement('div');
    div1.classList.add("course-preview");
    div1.innerHTML=`
    <h2>`+Course+`</h2>
    <button class="btn" id="${Course}">Continue</button>`;
    div.appendChild(div1);
  });

var all_button = document.getElementsByClassName('btn');
  for (var i = 0 ; i < all_button.length; i++) {
    all_button[i].addEventListener('click' , log , false ) ; 
  }



  let db = new sqlite3.Database('../db.sqlite3', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the chinook database.');
  });