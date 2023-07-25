document.addEventListener('DOMContentLoaded', function () {

    new ClipboardJS('.btn');

    document.querySelectorAll('.btn').forEach(function (button) {
        button.addEventListener('click', function () {
            button.textContent = 'Copied!';
            setTimeout(function () {
                button.textContent = 'Copy';
            }, 1000);
        });
    });
});