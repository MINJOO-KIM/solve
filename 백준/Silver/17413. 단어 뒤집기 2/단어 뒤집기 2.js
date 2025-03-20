let input = [];

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.on("line", (line) => {
  input = line.split("");
});

readline.on("close", () => {
  solution(input);
  process.exit();
});

const solution = (inp) => {
  let str = [];
  let ans = "";
  let temp = "";
  let tag = ">";

  for (let a of inp) {
    if (a === "<") {
      tag = "<";
      ans += temp.split("").reverse().join("") + a;
      temp = "";
    } else if (a === ">") {
      tag = ">";
      ans += temp + a;
      temp = "";
    } else if (a === " ") {
      if (tag === "<") {
        ans += temp;
      } else {
        ans += temp.split("").reverse().join("");
      }
      ans += " ";
      temp = "";
    } else {
      temp += a;
    }
  }
  ans += temp.split("").reverse().join("");
  console.log(ans);
};