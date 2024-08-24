const homeScore = document.querySelector("#home_score");
const guestScore = document.querySelector("#guest_score");
const home1 = document.querySelector("#home_1");
const home2 = document.querySelector("#home_2");
const home3 = document.querySelector("#home_3");
const guest1 = document.querySelector("#guest_1");
const guest2 = document.querySelector("#guest_2");
const guest3 = document.querySelector("#guest_3");

let homeGoals = 0;
let guestGoals = 0;

function addOnePoint_Home() {
  homeGoals += 1;
  homeScore.textContent = homeGoals;
}
function addTwoPoint_Home() {
  homeGoals += 2;
  homeScore.textContent = homeGoals;
}
function addThreePoint_Home() {
  homeGoals += 3;
  homeScore.textContent = homeGoals;
}
function addOnePoint_Guest() {
  guestGoals += 1;
  guestScore.textContent = guestGoals;
}
function addTwoPoint_Guest() {
  guestGoals += 2;
  guestScore.textContent = guestGoals;
}
function addThreePoint_Guest() {
  guestGoals += 3;
  guestScore.textContent = guestGoals;
}

home1.onclick = addOnePoint_Home;
home2.onclick = addTwoPoint_Home;
home3.onclick = addThreePoint_Home;
guest1.onclick = addOnePoint_Guest;
guest2.onclick = addTwoPoint_Guest;
guest3.onclick = addThreePoint_Guest;

// homeScore.onclick = see;
// homeScore.addEventListener("click", () => {
//   seeH();
// });
// guestScore.addEventListener("click", () => {
//   seeG();
// });
