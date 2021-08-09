    topics = document.getElementsByClassName('topicsContent');
    for (i = 0; i<topics.length; i++){
        if(topics[i].getBoundingClientRect().height>120){
            topics[i].style.height = topics[i].getBoundingClientRect().height - 120 + 'px'
        }
    }


    function checkIfFooterFixed(){
        footerBottom = document.getElementsByTagName('footer')[0].getBoundingClientRect().bottom;
        if(footerBottom<window.innerHeight){
            document.getElementsByTagName('footer')[0].style.position = 'fixed';
            document.getElementsByTagName('footer')[0].style.bottom = '0';
        }else{
            document.getElementsByTagName('footer')[0].style.position = 'relative';
        }
    }

    function returnToIndex(){
        window.location.href = "/";

    }

    checkIfFooterFixed();
