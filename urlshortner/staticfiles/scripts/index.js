const short_linkEl=document.querySelector('.short_link');
const copied_El=document.querySelector('.copied')

short_linkEl.addEventListener('click', (target)=>{

         if(short_linkEl.value){  // if the field has text, 

         navigator.clipboard.writeText(short_linkEl.value);
         copied_El.innerText='Copied!!'
         copied_El.style.color='dark'
         setTimeout(() => {
            copied_El.innerText=''
         }, 1000); 
      }

})