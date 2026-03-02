// Change this if your FastAPI runs elsewhere.
const API_BASE = "http://127.0.0.1:8080";

const out = document.getElementById("output");
function show(obj) {
  out.textContent = typeof obj === "string" ? obj : JSON.stringify(obj, null, 2);
}

async function request(path, options = {}) {
  const url = API_BASE + path;
  try {
    const res = await fetch(url, {
      headers: { "Content-Type": "application/json", ...(options.headers || {}) },
      ...options,
    });

    const text = await res.text();
    let data;
    try { data = text ? JSON.parse(text) : null; } catch { data = text; }

    if (!res.ok) {
      show({ error: true, status: res.status, statusText: res.statusText, url, response: data });
      return;
    }
    show({ ok: true, status: res.status, url, response: data });
  } catch (e) {
    show({ error: true, message: String(e), url });
  }
}

// Movies
document.getElementById("btnGetMovies").onclick = () =>
  request("/movies", { method: "GET" });

document.getElementById("btnGetMovieById").onclick = () => {
  const id = document.getElementById("movieIdGet").value.trim();
  request(`/movies/${encodeURIComponent(id)}`, { method: "GET" });
};

document.getElementById("btnCreateMovie").onclick = () => {
  const body = {
    title: document.getElementById("movieTitle").value,
    release_year: Number(document.getElementById("movieYear").value),
    runtime_minutes: Number(document.getElementById("movieRuntime").value),
    genre: document.getElementById("movieGenre").value,
  };
  request("/movies", { method: "POST", body: JSON.stringify(body) });
};

document.getElementById("btnUpdateMovie").onclick = () => {
  const id = document.getElementById("movieIdUpdate").value.trim();
  const body = {
    title: document.getElementById("movieTitleU").value,
    release_year: Number(document.getElementById("movieYearU").value),
    runtime_minutes: Number(document.getElementById("movieRuntimeU").value),
    genre: document.getElementById("movieGenreU").value,
  };
  request(`/movies/${encodeURIComponent(id)}`, { method: "PUT", body: JSON.stringify(body) });
};

document.getElementById("btnDeleteMovie").onclick = () => {
  const id = document.getElementById("movieIdDelete").value.trim();
  request(`/movies/${encodeURIComponent(id)}`, { method: "DELETE" });
};

// Lists
document.getElementById("btnGetListsByUser").onclick = () => {
  const userId = document.getElementById("userIdLists").value.trim();
  request(`/users/${encodeURIComponent(userId)}/lists`, { method: "GET" });
};

document.getElementById("btnCreateList").onclick = () => {
  const userId = document.getElementById("userIdCreateList").value.trim();
  const body = { name: document.getElementById("listName").value };
  request(`/users/${encodeURIComponent(userId)}/lists`, { method: "POST", body: JSON.stringify(body) });
};

document.getElementById("btnUpdateList").onclick = () => {
  const listId = document.getElementById("listIdUpdate").value.trim();
  const body = { name: document.getElementById("listNameU").value };
  request(`/lists/${encodeURIComponent(listId)}`, { method: "PUT", body: JSON.stringify(body) });
};