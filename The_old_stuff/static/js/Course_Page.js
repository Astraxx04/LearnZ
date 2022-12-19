
//Course name - Key,, current chapter - 0 index,, chapter name - 1 index
const Courses={"JavaScript Fundamentals": ["Chapter 4","Callbacks & Closures"],"Data Science": ["Chapter 4","Callbacks & Closures"],"C programming": ["Chapter 4","Callbacks & Closures"],"Data Communication": ["Chapter 4","Callbacks & Closures"],"Data structure Fundamentals": ["Chapter 4","Callbacks & Closures"],"Micro Processor": ["Chapter 4","Callbacks & Closures"]};


const CourseContainer = document.getElementById("CourseContainer");  
//For Every person insert card 
Object.keys(Courses).forEach(Course => {
    //Creted div with class card;
    var div = document.createElement('div');
    div.classList.add("card");
    CourseContainer.appendChild(div);
    //Creted div with class course-preview and make card as parent;
    var div1 = document.createElement('div');
    div1.classList.add("course-preview");
    div1.innerHTML=`<h6>Course</h6>
    <h2>`+Course+`</h2>
    <a href="#"
      >View all chapters <i class="fas fa-chevron-right"></i
    ></a>`;
    div.appendChild(div1);
     //Creted div with class course-info and make content as card;
    var div2 = document.createElement('div');
    div2.classList.add("course-info");
    div2.innerHTML=`<h6>`+Courses[Course][0]+`</h6>
    <h2>`+Courses[Course][1]+`</h2>
    <button class="btn">Continue</button>`;
    div.appendChild(div2);
  });