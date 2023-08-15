function copyBtn(uri) {
    navigator.clipboard.writeText(uri);
    alert("saved uri " + uri);
}