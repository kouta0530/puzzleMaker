const container = document.querySelector(".puzzle-container");
let reading = false;
let loadedContents = 0;

console.log("hello world");

window.addEventListener("scroll", (e) => {
  if (!reading) {
    const bodyHeight = document.body.clientHeight;
    const windowHeight = window.innerHeight;
    const bottomPoint = bodyHeight - windowHeight;
    const currentPoint = window.pageYOffset;

    if (bottomPoint <= currentPoint) {
      reading = false;
      const div = document.createElement("div");
      div.classList.add("puzzle");
      div.innerHTML = `
        <div>           
          <img src="static/img/no_image.png" alt={{p.title}} class="puzzle-picture" >
        </div>
        <div>
          <img src="" alt="投稿者アイコン" class="user-icon">
          <p>モックタイトル</p>
        </div>
      `;

      container.appendChild(div);
    }
  }
});
