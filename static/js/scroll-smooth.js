document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

$(window).scroll(function () {
            if ($(window).width() <= 760) {
                if ($(this).scrollTop() > 600) {
                    $('.display-phone').hide();
                } else {
                    $('.display-phone').fadeIn();
                }
            }
        });