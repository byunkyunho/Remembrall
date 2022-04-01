function visible_word(what_checkbox)
{   
    if(!(document.querySelector("#visible_mean").checked) && !(document.querySelector("#visible_eng").checked))
    {
        document.querySelector("#"+what_checkbox).checked = true
    }

    eng_list =  document.querySelectorAll("#eng")
    mean_list = document.querySelectorAll("#mean")
    dash_list = document.querySelectorAll("#middle_dash")

    for(var i=0;i<eng_list.length;i++)
    {
        if(document.querySelector("#visible_mean").checked && document.querySelector("#visible_eng").checked){
            // eng_list[i].style.visibility = 'visible'
            // mean_list[i].style.visibility = 'visible'   
            eng_list[i].style.display = 'inline'
            mean_list[i].style.display = 'inline'     
            dash_list[i].style.display = 'inline'    
        }
        else if(document.querySelector("#visible_eng").checked)
        {
            // eng_list[i].style.visibility = 'visible'
            // mean_list[i].style.visibility = 'hidden'
            eng_list[i].style.display = 'inline'
            mean_list[i].style.display = 'none'
            dash_list[i].style.display = 'none'
        }    
        else
        {
            // eng_list[i].style.visibility = 'hidden'
            // mean_list[i].style.visibility = 'visible'
            eng_list[i].style.display = 'none'
            mean_list[i].style.display = 'inline'
            dash_list[i].style.display = 'none'

        }
    }
    
}
