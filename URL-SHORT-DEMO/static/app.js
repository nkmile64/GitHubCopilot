function showLink(el, url) {
  const a = document.createElement("a");
  a.href = url;
  a.textContent = url;
  a.target = "_blank";
  a.rel = "noopener";
  el.className = "output";
  el.replaceChildren(a);
}

function showError(el, message) {
  el.className = "output error";
  el.textContent = message;
}

async function post(path, options) {
  const res = await fetch(path, options);
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const detail = data.detail;
    throw new Error(typeof detail === "string" ? detail : "Invalid input");
  }
  return data;
}

document.getElementById("shorten-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const out = document.getElementById("shorten-output");
  try {
    const data = await post("/api/shorten", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: document.getElementById("long-url").value }),
    });
    showLink(out, data.short_url);
  } catch (err) {
    showError(out, err.message);
  }
});

document.getElementById("lookup-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const out = document.getElementById("lookup-output");
  const short = document.getElementById("short-url").value;
  try {
    const data = await post(`/api/resolve?short=${encodeURIComponent(short)}`);
    showLink(out, data.url);
  } catch (err) {
    showError(out, err.message);
  }
});
