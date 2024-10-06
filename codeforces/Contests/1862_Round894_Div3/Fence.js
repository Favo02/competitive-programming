var fs = require("fs")
var stdinBuffer = fs.readFileSync(0)
const input = stdinBuffer.toString().split("\n").splice(1)
input.pop()


const res = []
outloop:
for (let i = 0; i < input.length; i+=2) {
  // for (let i = 0; i < 1; i+=2) {
  const element = input[i+1]
  const arr = element.split(" ").map(e => parseInt(e))

  // console.log(arr)
  
  const mat = []
  const MAX = arr[0]
  
  for (let i = 0; i < MAX; i++) {
    // console.log(arr[i])
    if (arr[i]) {
      mat.push(Array(arr[i]).fill(true))
      while (mat[i].length < MAX) {
        mat[i].push(" ")
      }
    }
    else {
      mat.push(Array(MAX).fill(false))
    }
  }

  // console.log(mat)
  
  for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j < mat[i].length; j++) {

      // console.log(i, j)
      
      if (mat[i][j] !== mat[j][i]) {
        res.push("no")
        continue outloop;
      }

    }
  }

  res.push("yes")
  

}

console.log(res.join("\n"))
