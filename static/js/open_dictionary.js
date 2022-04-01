function open_dictionary(word, lang){
    if(lang==='en'){
        window.open("https://en.dict.naver.com/#/search?query="+word); 
    }
    else if(lang==='kor'){
        window.open("https://ko.dict.naver.com/#/search?query="+word);   
    }
}