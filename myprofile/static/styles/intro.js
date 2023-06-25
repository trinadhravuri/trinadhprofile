
let time = document.getElementById('timedisplay');
let d = new Date();
time.innerHTML = d.toLocaleTimeString();
const hours = d.getHours();
time.innerHTML = hours;
if (hours > 4 && hours< 10){
    time.innerHTML = 'Good Morning..Have a Nice day!';
}
else if (hours>= 10 && hours < 12){
    time.innerHTML = "Good day..";
} 
else if (hours>= 12 && hours < 17){
    time.innerHTML = "Good Afternoon..";
} 
else if (hours>= 17 && hours < 21){
    time.innerHTML = "Have a Nice Evening..";
} 
else if (hours>= 21 && hours < 24){
    time.innerHTML = "Time to have a Great Sleep ..";
} 
else{
    time.innerHTML = NaN;
}
