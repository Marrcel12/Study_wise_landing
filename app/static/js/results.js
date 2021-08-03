    topics = document.getElementsByClassName('topicsContent');
    for (i = 0; i<topics.length; i++){
        if(topics[i].getBoundingClientRect().height>120){
            topics[i].style.height = topics[i].getBoundingClientRect().height - 120 + 'px'
        }
    }

    function returnToIndex(){
        window.location.href = "/";

    }