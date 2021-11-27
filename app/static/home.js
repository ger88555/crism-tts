$(function () {
    const FORM = $('#TTSForm');
    const SOURCE_RADIOS = $('input[name="source_option"]', FORM);
    const SOURCE_INPUTS = $('.form-control', FORM)
    const SUBMIT_BUTTON = $('button[type="submit"]', FORM);


    /**
     * Disable all but the nearest field when selecting a source option.
     */
    $(SOURCE_RADIOS).on('change', function () {
        $(SOURCE_INPUTS).attr('disabled', true);
        $( '#' + $(this).data('field') ).attr('disabled', false);
    });

    /**
     * Discard empty fields on submit.
     */
    $(FORM).on('submit', function(e) {
        e.preventDefault();
        $(SUBMIT_BUTTON).attr('disabled', true);

        // Disable empty input.
        $(SOURCE_RADIOS).attr('disabled', true);
        $(SOURCE_INPUTS)
            .filter(function () { return $(this).val() == "" })
            .attr('disabled', true);

        $(FORM).unbind('submit').submit();
    });
});