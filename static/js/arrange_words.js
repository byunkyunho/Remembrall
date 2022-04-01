function arrange_words(by_what) {
    if(by_what==='date'){
        document.querySelector('#word_by_spell').style.display = 'none'
        document.querySelector('#word_by_date').style.display = 'block'
    }
    else{
        document.querySelector('#word_by_spell').style.display = 'block'
        document.querySelector('#word_by_date').style.display = 'none'
    }
}