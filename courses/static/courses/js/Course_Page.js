var NoOfSemester = 7;
var currentSem = 1;
var data = document.currentScript.dataset;
var user_usn = data.usn;
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
  sessionStorage.setItem("courseStudent", course_name);
  // console.log(sessionStorage.getItem("course"));
  location.assign("/features");
}

//For Every course insert card 
courses[currentSem][0].forEach(Course => {
    //Creted div with class card;
    var div = document.createElement('div');
    div.classList.add("card");
    CourseContainer.appendChild(div);
    //Creted div with class course-preview and make card as parent;
    var div1 = document.createElement('div');
    div1.classList.add("course-preview");
    div1.innerHTML=`
    <h2>`+Course[0]+`</h2>
    <button class="btn" id="${Course[0]}">Continue</button>`;
    div.appendChild(div1);
  });

var all_button = document.getElementsByClassName('btn');
  for (var i = 0 ; i < all_button.length; i++) {
    all_button[i].addEventListener('click' , log , false ) ; 
  }


