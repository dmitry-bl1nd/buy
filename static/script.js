new WOW().init();

let input = document.querySelectorAll('form p');
 for (let i = input.length - 1; i >= 0; i--) {
 	console.dir(input[i]);
 	input[i].classList.add('form-control');
 	input[i].classList.add('md-6');
 }
    
