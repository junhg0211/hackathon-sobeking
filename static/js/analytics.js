let paragraph = document.querySelector("#contents-tag");

if (target == 'week' || target == 'month') {
    fetch(`/api/ask/${target}`).then(r => {
        r.json().then(j => {
            paragraph.innerText = j['message'];
        });
    });
}
