$(document).ready(function () {
    $('button[name="action"][value="continue"]').click(function (e) {
        $('#new-prompt-group').show();
    });

    $('#describe-form').on('submit', function (e) {
        const userPrompt = $('#user_prompt').val();
        if (userPrompt.trim() === '') {
            e.preventDefault();
            alert('Please enter a description for the email.');
        }
    });
});
