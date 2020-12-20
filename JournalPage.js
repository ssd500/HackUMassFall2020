//second page

function process(){   
    const mood = window.localStorage.getItem('clicked');
    console.log(mood)
    var root = document.getElementsByTagName('html')[0]; 

    if (mood  === 'Happy'){
        root.setAttribute('class', 'Happy');
    }

    else if (mood === 'Happy') {
        root.setAttribute('class', 'Happy');
    }

    else if (mood === '') {
        root.setAttribute('class', 'Happy');
    }

    else if (mood === '') {
        root.setAttribute('class', 'Happy');
    }

    else if (mood === '') {
        root.setAttribute('class', 'Happy');
    }

    else if (mood === '') {
        root.setAttribute('class', 'Happy');
    }

    else if (mood === '') {
        root.setAttribute('class', 'Happy');
    }

 }
 
 window.onload = process;
