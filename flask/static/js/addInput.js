$(function()
{
    $(document).on('click', '.btn-add', function(e)
    {
        e.preventDefault();
        var current = $('.entry').length;
	if (current == 12) {
            if (!($('.inputAlert').length)) {
	        $('.inputs').append(("<h4 class=inputAlert>You cannot add more than 12 fields</h4>"));
	    }
	    return false;
	}
        var controlForm = $('.controls div:first'),
            currentEntry = $(this).parents('.entry:first'),
            newEntry = $(currentEntry.clone()).appendTo(controlForm);

        newEntry.find('input').val('');
        controlForm.find('.entry:not(:last) .btn-add')
            .removeClass('btn-add').addClass('btn-remove')
            .removeClass('btn-primary').addClass('btn-danger')
            .html('<span class="glyphicon glyphicon-minus"></span>');
    }).on('click', '.btn-remove', function(e)
    {
        var current = $('.entry').length;
	if (current <=12) {
            $('.inputAlert').remove();
	}
	$(this).parents('.entry:first').remove();
	e.preventDefault();
	return false;
    });
});
