document.getElementById("index_form").addEventListener("submit", (e) => {
  e.preventDefault();

  const data = new FormData(e.currentTarget);

  url_imput = data.get("url_input");

  console.log(shorten_link(url_imput));
});
