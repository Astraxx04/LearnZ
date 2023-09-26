
//Person Name - Key,, github - 0 index,, linkdin - 1 index,, imagepath - 2 index

const Peoples = {
  "SYLLABUS": ["FrontEnd", "https://github.com/Bhawesh02", "https://www.linkedin.com/in/bhawesh-agarwal-70b98b113/", "../images/creator/me.jpg"],
  "QUIZ": ["Frontend", "https://github.com/Sonuuuuuuu", "https://www.linkedin.com/in/konjeti-nidhi-96245a226/", "../images/creator/me.jpg"], "MATERIAL": ["Frontend", "https://github.com/Sonuuuuuuu", "https://www.linkedin.com/in/konjeti-nidhi-96245a226/", "../images/creator/me.jpg"],
  "": ["Frontend", "https://github.com/Sonuuuuuuu", "https://www.linkedin.com/in/konjeti-nidhi-96245a226/", "../images/creator/me.jpg"]
};


const CardContainer = document.getElementById("CardContainer");
//For Every person insert card 
Object.keys(Peoples).forEach(People => {
  //Creted div with class div;
  var div = document.createElement('div');
  div.classList.add("card");
  CardContainer.appendChild(div);
  //Creted div with class content and make card as parent;
  var div1 = document.createElement('div');
  div1.classList.add("content");
  div.appendChild(div1);
  //Creted div with class imgbx and make content as parent;
  var div2 = document.createElement('div');
  div2.classList.add("imgBx");
  div1.appendChild(div2);
  //create img with imgbx as parent
  var img = document.createElement('img');
  img.setAttribute("src", Peoples[People][3]);
  div2.appendChild(img);
  //Creted div with class contentBx and make content as parent
  var div4 = document.createElement('div');
  div4.classList.add("contentBx");
  div4.innerHTML = "<h3>" + People + "<br /><span>" + Peoples[People][0] + "</span></h3>";
  div1.appendChild(div4);
  //added git and likdin to card as parent
  var ul = document.createElement('ul');
  ul.classList.add("sci");
  div.appendChild(ul);
  var li = document.createElement('li');
  li.setAttribute("style", "\"--i: 1\"")
  li.innerHTML = "<a href=\"" + Peoples[People][1] + "\"><i class=\"fa-brands fa-github\"></i></a>";
  ul.appendChild(li);
  var li1 = document.createElement('li');
  li1.setAttribute("style", "\"--i: 1\"")
  li1.innerHTML = "<a href=\"" + Peoples[People][2] + "\"><i class=\"fa-brands fa-linkedin\"></i></a>";
  ul.appendChild(li1);

});