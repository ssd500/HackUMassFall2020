//first page
function process(){   
   const moods = ["Mellow", "Melancholy", "Happy", "Sad", "Angry", "Cheerful"];

    for(mood of moods){
        const button = document.getElementById(mood).addEventListener('click',function(){
            window.localStorage.removeItem('clicked');
            window.localStorage.setItem("clicked", this.id);
            console.log('Donezo');
            //html links to the second page
        });
    }
}
console.log('connected');
window.onload = process;

//Animation code






