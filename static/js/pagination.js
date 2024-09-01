document.addEventListener('DOMContentLoaded', () => {
    const products = document.querySelectorAll('.product-card');
    const itemsPerPage = 3; // Number of items per page
    let currentPage = 1;

    function showPage(page) {
        products.forEach((product, index) => {
            product.style.display = 'none';
            if (index >= (page - 1) * itemsPerPage && index < page * itemsPerPage) {
                product.style.display = 'block';
            }
        });
    }

    function updatePaginator() {
        const pageNumbers = document.querySelector('.page-numbers');
        pageNumbers.textContent = currentPage;
    }

    document.querySelector('.prev').addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
            updatePaginator();
        }
    });

    document.querySelector('.next').addEventListener('click', () => {
        if (currentPage < Math.ceil(products.length / itemsPerPage)) {
            currentPage++;
            showPage(currentPage);
            updatePaginator();
        }
    });

    // Initialize paginator
    showPage(currentPage);
    updatePaginator();
});
