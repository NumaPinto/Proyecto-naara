function openModal(imageName) {
    var modal = document.getElementById("modal");
    var modalImage = document.getElementById("modal-image");
    modal.style.display = "block";
    modalImage.src = "images/" + imageName;
}

function closeModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}
