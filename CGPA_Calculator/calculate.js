const formElement = document.getElementById("score-form");
const creditScores = {
  "S": 10,
  "A": 9,
  "B": 8,
  "C": 7,
  "D": 5,
  "E": 4,
  "F": 0,
};

const credits = {};

const grades = {};

formElement.addEventListener("submit", function (event) {
  event.preventDefault();
  let i = 0;
  while (i < 16) {
    formElement[i].value.trim();
    if (i % 2 == 0) {
      if (formElement[i].value.trim() == "") {
        credits[Math.floor(i / 2) + 1] = 0;
      } else {
        credits[Math.floor(i / 2) + 1] = formElement[i].value.split(" ");
      }
    } else {
      if (formElement[i].value.trim() == "") {
        grades[Math.floor(i / 2) + 1] = 0;
      } else {
        grades[Math.floor(i / 2) + 1] = formElement[i].value.split(" ");
      }
    }
    i++;
  }

  let total = 0;
  let creditTotal = 0;
  for (let j = 1; j <= 8; j++) {
    if (credits[j] == 0) {
      break;
    }
    for (let k = 0; k < credits[j].length; k++) {
      total += (Number(credits[j][k]) * creditScores[grades[j][k]]);
      creditTotal += Number(credits[j][k]);
    }
    console.log(total);
  }

  const cgpa = total / creditTotal;
  const cgpaConElement = document.getElementById("cgpa-con");
  const cgpaElement = document.getElementById("cgpa");
  cgpaElement.innerText = cgpa.toFixed(2);
  cgpaConElement.style.display = "block";
});
