var Tabs = (function(wrapper) {
    wrapper.find('ul.tabs').on('click', 'a', function(e) {
        e.preventDefault();
        var tabName = $(this).parent().data('tab');
        wrapper.find('.tab-content').removeClass('active');
        wrapper.find('.tab-content.' + tabName).addClass('active');
        wrapper.find('ul.tabs li').removeClass('active');
        $(this).parent().addClass('active');
    });
});
