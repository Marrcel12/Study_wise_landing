$(document).ready(function () {
    $('.js-example-basic-multiple').select2({
        placeholder: "Czego chciałbyś się dziś nauczyć"
    });
});

function scrollDown() {
    window.scrollBy(0, window.innerHeight);
}

function submitForm() {
    if ($('.js-example-basic-multiple')[0].value.length > 0) {
        $('#searchForm').submit();
    }
}
window.addEventListener("keyup", detectButton);

function detectButton(e) {
    if (e.code == "Enter") {
        submitForm()
    }
}

function openIg(){
    window.open('https://www.instagram.com/studywise.pl/', '_blank').focus();
}

var tempHref = document.location.href;
tempHref = tempHref.replace('127.0.0.1:5000', 'studywise.pl')
console.log(tempHref)
window.history.pushState("/test", "", '');
//document.location.href = tempHref;
