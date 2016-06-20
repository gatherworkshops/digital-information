// generates the chapter dropdown menu from a json file
$(document).ready( function() {

    // updates the nav with data fetched from the course's JSON.
    // we do this via JSON to avoid the need for repetition of
    // sitemap or coursemap data in a place other than the course's
    // root directory, as Jekyll can only read custom data from the
    // _data dir which is not ideal.
    function generateMenu(course) {

        // find all elements we will modify
        var navBar = $('#page-navigation');
        var courseName = navBar.find('.course-name');
        var chapterDropdown = navBar.find('.dropdown-menu');

        // update the course name in the nav bar
        courseName.html(course.title);

        // create and append a menu item for each chapter
        $.each(course.chapters, function(index, chapter){
            var chapterLink = $(
                '<li>' +
                    '<a href="' + this.name + '">' +
                        this.title +
                    '</a>' +
                '</li>'
            );
            chapterDropdown.append(chapterLink);
        });

        // show all hidden nav elements
        navBar
            .find('.invisible')
            .removeClass('invisible');
    }

    // go get the course data
    $.get( "index.json", generateMenu);

});