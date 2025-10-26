// Professional Advanced Navbar JavaScript Functionality

$(document).ready(function() {
    // Navbar scroll effect
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 50) {
            $('.navbar').addClass('scrolled');
        } else {
            $('.navbar').removeClass('scrolled');
        }
    });
    
    // Handle dropdown toggle on mobile
    $('.dropdown-toggle').on('click', function(e) {
        if ($(window).width() <= 768) {
            // Let Bootstrap handle the dropdown toggle
            // But prevent the default link behavior
            e.preventDefault();
            
            // Get the dropdown menu
            var $dropdown = $(this).parent('.dropdown');
            var $menu = $dropdown.find('.dropdown-menu');
            
            // Close other dropdowns
            $('.dropdown').not($dropdown).removeClass('show').find('.dropdown-menu').removeClass('show');
            
            // Toggle current dropdown using Bootstrap's classes
            $dropdown.toggleClass('show');
            $menu.toggleClass('show');
        }
    });
    
    // Close dropdowns when clicking outside
    $(document).on('click', function(e) {
        if (!$(e.target).closest('.dropdown').length && $(window).width() <= 768) {
            $('.dropdown').removeClass('show').find('.dropdown-menu').removeClass('show');
        }
    });
    
    // Prevent dropdown from closing when clicking inside
    $('.dropdown-menu').on('click', function(e) {
        e.stopPropagation();
    });
    
    // Add ripple effect to buttons
    $('.btn-hover-effect').on('click', function(e) {
        var $btn = $(this);
        var x = e.pageX - $btn.offset().left;
        var y = e.pageY - $btn.offset().top;
        
        var $ripple = $('<span class="ripple"></span>');
        $ripple.css({
            top: y,
            left: x
        });
        
        $btn.append($ripple);
        
        setTimeout(function() {
            $ripple.remove();
        }, 600);
    });
    
    // Handle window resize
    $(window).on('resize', function() {
        if ($(window).width() > 768) {
            $('.dropdown-menu').removeClass('show');
            $('.dropdown').removeClass('show');
        }
    });
});