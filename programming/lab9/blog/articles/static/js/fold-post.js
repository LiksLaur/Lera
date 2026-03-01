document.querySelectorAll('.fold-button').forEach(btn => {
    btn.addEventListener('click', function() {
        const post = this.closest('.one-post');
        if (post) {
            post.classList.toggle('folded');
            this.textContent = post.classList.contains('folded') ? 'развернуть' : 'свернуть';
        }
    });
});