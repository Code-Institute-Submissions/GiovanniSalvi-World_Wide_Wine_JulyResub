$('.nav-link').on('click', function () {
    if(!$(this).siblings('.nav-link').hasClass('collapsed')) {
       $(this).siblings('.nav-link').click();
       }
    });