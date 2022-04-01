function delete_words(){
    word_check_list = document.querySelectorAll(".word_checkbox");
    checked_word = []
    
    for(var i=0; i<word_check_list.length;i++){
        if(word_check_list[i].checked)
        {
            checked_word.push(word_check_list[i].name);
            
        }
    }

    send_delete_request(checked_word)
 
}
function send_delete_request(words){
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
    
    xhr.open('GET', 'http://172.30.1.34:8000/delete_words/'+words.join(","));
    xhr.send();
}