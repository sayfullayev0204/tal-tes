const circles = document.querySelectorAll('.circle');
const popup = document.getElementById('popup');
const popupImg = document.getElementById('popup-img');
const popupTitle = document.getElementById('popup-title');
const popupDesc = document.getElementById('popup-desc');

circles.forEach(circle => {
    circle.addEventListener('click', (e) => {
        const name = e.target.dataset.name;
        const image = e.target.dataset.image;
        const desc = e.target.dataset.desc;

        popupImg.src = image;
        popupTitle.textContent = name;
        popupDesc.textContent = desc;

        popup.style.display = 'block';
        popup.style.left = e.pageX + 'px';
        popup.style.top = e.pageY + 'px';
    });
});

// Popup-ni yashirish uchun
document.addEventListener('click', (e) => {
    if (!e.target.classList.contains('circle')) {
        popup.style.display = 'none';
    }
});

const regions = document.querySelectorAll('.region');
const infoBox = document.getElementById('info-box');

regions.forEach(region => {
    region.addEventListener('mouseover', (e) => {
        const name = e.target.dataset.name;
        infoBox.style.display = 'block';
        infoBox.textContent = name;
        infoBox.style.left = e.pageX + 'px';
        infoBox.style.top = e.pageY + 'px';
    });

    region.addEventListener('mouseout', () => {
        infoBox.style.display = 'none';
    });
});