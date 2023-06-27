setTimeout(function () {
  window.location.reload();
}, 5000);
// const waterLevelLiquid = document.querySelector(".water__liquid"),
//   waterLevelStatus = document.querySelector(".water__status"),
//   waterLevelPercentage = document.querySelector(".water__percentage");

// const waterLevelNumber = document.getElementById("level-number").children[0];

// function getLevel() {
//   $.ajax({
//     url: "API.txt",
//     dataType: "text",
//     success: function (text) {
//       $("#level-number").text(text);

//       let level = Math.floor(parseInt(text));
//       waterLevelPercentage.innerHTML = level + "%";

//       waterLevelLiquid.style.height = `${level}%`;

//       if (level >= 100) {
//         waterLevelStatus.innerHTML = `Full of Water <i class="ri-water-flash-fill animated-green"></i>`;
//         waterLevelLiquid.style.height = "103%";
//       } else if (level <= 20) {
//         waterLevelStatus.innerHTML = `Low Water Level <i class="ri-contrast-drop-2-line animated-red"></i>`;
//       } else {
//         waterLevelStatus.innerHTML = "";
//       }

//       if (level <= 20) {
//         waterLevelLiquid.classList.add("gradient-color-red");
//         waterLevelLiquid.classList.remove(
//           "gradient-color-orange",
//           "gradient-color-yellow",
//           "gradient-color-green"
//         );
//       } else if (level <= 40) {
//         waterLevelLiquid.classList.add("gradient-color-orange");
//         waterLevelLiquid.classList.remove(
//           "gradient-color-red",
//           "gradient-color-yellow",
//           "gradient-color-green"
//         );
//       } else if (level <= 80) {
//         waterLevelLiquid.classList.add("gradient-color-yellow");
//         waterLevelLiquid.classList.remove(
//           "gradient-color-red",
//           "gradient-color-orange",
//           "gradient-color-green"
//         );
//       } else {
//         waterLevelLiquid.classList.add("gradient-color-green");
//         waterLevelLiquid.classList.remove(
//           "gradient-color-red",
//           "gradient-color-orange",
//           "gradient-color-yellow"
//         );
//       }

//       setTimeout(getLog, 5000);
//     },
//   });
// }

// getLevel();
