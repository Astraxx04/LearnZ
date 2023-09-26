let apiKey = "AIzaSyCvkzPpAD2b-_zcD_NLT07cUZTdYuk0XlU"
$(document).ready(function(){
    //let apiKey = "AIzaSyCC5ewMqBnYXGeOL0Cu1Gi2N6gE3hSzvy0"
 
    //$("form").submit((e) => {
      //  e.preventDefault()
        //let search = $("#search").val()
        // videoSearch(apiKey,"three schema architecture",4)
        // videoSearch(apiKey,"dbms",2)
    //})
})
 
function videoSearch(apiKey,search,maxResults){

    $("#videos").empty()

    $.get("https://www.googleapis.com/youtube/v3/search?key=" + apiKey + "&type=video&part=snippet&maxResults=" + maxResults + "&q=" + search + "&sp=CAM%253D",(data) => {
        //console.log(data)
 
        let video = '';
 
        data.items.forEach(item => {
            video = `
            <iframe class = "video" src="http://www.youtube.com/embed/${item.id.videoId}" frameborder="0" allowfullscreen></iframe>
            `;
            $("#videos").append(video);
        });
    })
}

var dat = [];
//fetch function
fetch('/static/features/json/data.json').then(
    function(u){ return u.json();}
    ).then(
    function(json){
    data_function(json); //calling and passing json to another function data_function
    }
    )
    
//  Accessing the list of keywords
function data_function(data){
    data.forEach(function (da) {
        dat.push(da);
    });
    var lenmax = dat.length;
    //console.log(dat)
    searchkey(0, lenmax, dat);
}
  


function searchkey(min, max, keyser){
    
    ranvar=getRandomNonRepeatingNumbers(min, max-1, 5);
    //console.log(ranvar);
    for(let xx=0;xx<5;xx++){
        //console.log(keyser[ranvar[xx]]);
        videoSearch(apiKey,keyser[ranvar[xx]],2);
    }
}

function getRandomNonRepeatingNumbers(min, max, count) {
  const result = [];
  const generatedNumbers = new Set();

  while (result.length < count) {
    const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;

    if (!generatedNumbers.has(randomNumber)) {
      result.push(randomNumber);
      generatedNumbers.add(randomNumber);
    }
  }

  return result;
}

