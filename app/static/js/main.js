$(document).ready(function () {
    $('.js-example-basic-multiple').select2();
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
