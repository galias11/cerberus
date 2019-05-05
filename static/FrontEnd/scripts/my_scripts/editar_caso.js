//$(document).ready(function () {
//    $('tr').click(function () {
//        $(this).remove();
//        return false;
//    });
//});
$("tr").click(function () {
    window.location = $(this).data("href");
});