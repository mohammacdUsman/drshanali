/* =======================================
   BLOG.JS — Search + Category Filter
======================================= */

const searchInput = document.getElementById('blogSearch');
const filterBtns = document.querySelectorAll('.filter-btn');
const blogCards = document.querySelectorAll('.blog-card');
const noResults = document.querySelector('.no-results');

let activeFilter = 'all';
let searchQuery = '';

function filterPosts() {
    let visible = 0;

    blogCards.forEach(card => {
        const title = card.querySelector('h3')?.textContent.toLowerCase() || '';
        const excerpt = card.querySelector('.blog-excerpt')?.textContent.toLowerCase() || '';
        const category = card.dataset.category?.toLowerCase() || '';

        const matchesSearch = !searchQuery || title.includes(searchQuery) || excerpt.includes(searchQuery);
        const matchesFilter = activeFilter === 'all' || category === activeFilter;

        if (matchesSearch && matchesFilter) {
            card.style.display = '';
            card.style.animation = 'fadeUp 0.4s ease forwards';
            visible++;
        } else {
            card.style.display = 'none';
        }
    });

    if (noResults) noResults.style.display = visible === 0 ? '' : 'none';
}

// Simple debounce to prevent frequent DOM updates
let searchTimeout;
if (searchInput) {
    searchInput.addEventListener('input', () => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            searchQuery = searchInput.value.toLowerCase().trim();
            filterPosts();
        }, 250);
    });
}

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.dataset.filter;
        filterPosts();
    });
});
