const API = 'http://localhost:5000/api';

async function fetchPosts(page=1) {
  const res = await fetch(`${API}/posts?page=${page}&per_page=10`);
  const data = await res.json();
  const container = document.getElementById('posts');
  container.innerHTML = '';
  data.posts.forEach(p => {
    const el = document.createElement('div');
    el.innerHTML = `<h3><a href="/post.html?post_id=${p.post_id}">${p.title}</a></h3>
                    <p>${p.content.substring(0,150)}...</p>
                    <small>${p.likes_count} likes • ${p.comments_count} comments</small>`;
    container.appendChild(el);
  });
}

// on load
fetchPosts();
