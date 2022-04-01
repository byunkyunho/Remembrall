function set_favorite_word(user_code, word, is_favorite){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === xhr.DONE) {
            if (xhr.status === 200 || xhr.status === 201) {
                console.log(xhr.responseText);
            } else {
                console.error(xhr.responseText);
            }
        }
    };
    xhr.open('GET','https://www.oneclickclass.kr/add_favorite_word/'+user_code+'/'+word );
    xhr.send();
    if(is_favorite){
        document.querySelector('#favorite_word').querySelector('#'+word).style.display = 'none';
        document.querySelector('#word_by_spell').querySelector('#'+word).style.display = 'block';
        document.querySelector('#word_by_date').querySelector('#'+word).style.display = 'block';
    }
    else{
        document.querySelector('#favorite_word').querySelector('#'+word).style.display = 'block';
        document.querySelector('#word_by_spell').querySelector('#'+word).style.display = 'none';
        document.querySelector('#word_by_date').querySelector('#'+word).style.display = 'none';
    }
}
