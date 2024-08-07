const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_review");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");
const ratingField = document.getElementsByName("rating");
const ratingLabels = document.querySelectorAll('.rating-container ul li label');

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Highlight stars when hovered over or selected

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

/**
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Fetches the content of the corresponding review.
 * - Populates the `reviewText` input/textarea with the review's content for editing.
 * - Populates the `ratingField` with the review's rating for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("data-review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        let reviewRating = parseInt(document.getElementById(`rating${reviewId}`).innerText.trim()); // Assuming rating is a number

        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);

        // Set the rating field and highlight the stars
        for (let radio of ratingField) {
            if (parseInt(radio.value) === reviewRating) {
                radio.checked = true;
                highlightStars(reviewRating - 1, ratingLabels); // Adjust index as rating is 1-based
            }
        }
    });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific review.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("data-review_id");
        deleteConfirm.href = `delete_review/${reviewId}`;
        deleteModal.show();
    });
}
