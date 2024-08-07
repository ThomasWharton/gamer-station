// Script to highlight star rating on hover and on checked

document.querySelectorAll('.rating-container ul li label').forEach((label, index, labels) => {
    label.addEventListener('mouseover', () => {
        highlightStars(index, labels);
    });

    label.addEventListener('mouseout', () => {
        resetStars(labels);
    });

    label.addEventListener('click', () => {
        selectStars(index, labels);
    });
});

function highlightStars(index, labels) {
    labels.forEach((label, i) => {
        label.querySelector('i').style.color = i <= index ? '#878E8D' : '#fff';
    });
}

function resetStars(labels) {
    const checkedIndex = Array.from(labels).findIndex(label => label.querySelector('input').checked);
    highlightStars(checkedIndex, labels);
}

function selectStars(index, labels) {
    labels[index].querySelector('input').checked = true;
    highlightStars(index, labels);
}