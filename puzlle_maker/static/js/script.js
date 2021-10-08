const container = document.querySelector(".puzzle-container");
let reading = false;
let loadedContents = 0;
let id = 0;

const showAdditionalArticle = (article) => {
  const div = document.createElement("div");
  div.classList.add("puzzle");
  div.innerHTML = `
        <div>           
          <img src="${article.picture_url}" alt="${article.title}" class="puzzle-picture" >
        </div>
        <div>
          <img src="" alt="投稿者アイコン" class="user-icon">
          <h3>${article.title}</h3>
        </div>
      `;
  container.appendChild(div);
};

window.addEventListener("scroll", (e) => {
  if (!reading) {
    const bodyHeight = document.body.clientHeight;
    const windowHeight = window.innerHeight;
    const bottomPoint = bodyHeight - windowHeight;
    const currentPoint = window.pageYOffset;

    if (bottomPoint <= currentPoint) {
      reading = true;
      fetch("http://" + window.location.host + `/puzzles/${id}`)
        .then((res) => res.json())
        .then((articles) => {
          for (article of articles) {
            showAdditionalArticle(article);
          }
          id += 1;
        })
        .catch((e) => {
          alert("取得に失敗しました");
        });
      reading = false;
    }
  }
});
