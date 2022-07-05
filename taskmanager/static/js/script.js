$(document).ready(function() {
    // initialize mobile side navbar
    // sideNav() is a pre-built function
    $(".sidenav").sidenav();


    //initialisation for the Add Tasks page date-picker
    $('.datepicker').datepicker();

    //initialisation for category_id select:
    //let categorypicker = document.querySelectorAll('select');
    //M.FormSelect.init(categorypicker);
    $('select').formSelect();

    //initialisation for home page collapsible tasks list
    $('.collapsible').collapsible();
})



