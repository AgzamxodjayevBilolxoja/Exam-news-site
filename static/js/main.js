function redirectToPage() {
    let select = document.getElementById("pageSelect");
    let selectedValue = select.value;
    if (selectedValue) {
        window.location.href = selectedValue;
    }
}
