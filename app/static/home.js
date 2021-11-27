$(function () {
    const FORM = $('#TTSForm');
    const SOURCE_RADIOS = $('input[name="source_option"]', FORM);
    const SOURCE_INPUTS = $('.form-control', FORM)
    const SUBMIT_BUTTON = $('button[type="submit"]', FORM);
    const ENDPOINT = "/read";
    
    const RESULT_DIALOG = $('#result');
    const AUDIO_EMBED = $('audio > source', RESULT_DIALOG);
    const DOWNLOAD_BUTTON = $('#download', RESULT_DIALOG);


    /**
     * Disable all but the nearest field when selecting a source option.
     */
    $(SOURCE_RADIOS).on('change', function () {
        $(SOURCE_INPUTS).attr('disabled', true);
        $( '#' + $(this).data('field') ).attr('disabled', false);
    });

    /**
     * Retrieve a speech from the server.
     */
    $(FORM).on('submit', function(e) {
        e.preventDefault();
        $(SUBMIT_BUTTON).attr('disabled', true);
        
        const xhr = new XMLHttpRequest();

        xhr.open('POST', ENDPOINT);
        xhr.onload = processResponse;
        
        xhr.send(new FormData(event.target))
    });


    /**
     * Process the server response.
     * 
     * @param {XMLHttpRequest} this
     */
    const processResponse = function () {
        if (this.status === 200) {
            const mime = this.getResponseHeader('Content-Type').split(';')[0];
            const blob = new Blob([this.response], { type: mime });
            const url = URL.createObjectURL(blob);

            setResult(url);

        } else {
            setError(this.responseText);
        }

        $(SUBMIT_BUTTON).attr('disabled', false);
    }

    /**
     * Get the form data.
     * 
     * @returns {Object} The data object.
     */
    const getData = function () {
        const field = $( '#' + $(SOURCE_RADIOS).filter(':checked').data('field') );
        const data = {}

        data[field.attr('name')] = field.val();

        return data;
    }

    /**
     * Show the audio result.
     * 
     * @param {string} url URL to the audio file.
     */
    const setResult = function (url) {
        RESULT_DIALOG.attr('hidden', false);

        AUDIO_EMBED.prop('src', url)
        DOWNLOAD_BUTTON.prop('href', url)
    }

    /**
     * Show an error message.
     * 
     * @param {string} message The message.
     */
    const setError = function (message) { 
        RESULT_DIALOG.attr('hidden', true);

        alert(message);
    }
});