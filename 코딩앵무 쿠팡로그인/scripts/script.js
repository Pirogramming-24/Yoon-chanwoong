window.onload=function(){

    const pw_show_hide = document.querySelector('.pw_show_hide');
    const input_id = document.querySelector('input[type=text]')
    const input_pw = document.querySelector('input[type=password]')
    const id_errer = document.querySelector('.id_error');
    const pw_errer = document.querySelector('.pw_error');
    console.log(pw_show_hide, input_id,input_pw,id_errer,pw_errer);

    input_id.addEventListener('click',function(){
        id_errer.style.display = 'block'
    })
    input_pw.addEventListener('click',function(){
        pw_errer.style.display = 'block'
    })

    let i = true;
    pw_show_hide.addEventListener('click',function(){
        if(i === true){
            pw_show_hide.style.backgroundPosition = '-126px 0' //감김
            i = false;
        } else {
            pw_show_hide.style.backgroundPosition = '-105px 0' //뜸
            i = true;
        };
    });

}//onload end