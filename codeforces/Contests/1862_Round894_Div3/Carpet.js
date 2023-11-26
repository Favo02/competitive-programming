var fs = require("fs")
var stdinBuffer = fs.readFileSync(0)
const input = stdinBuffer.toString().split("\n").splice(1)
input.pop()

const res = []

// console.log(input)

const carpets = []
let pos = -1

for (let i = 0; i < input.length; i++) {
  const el = input[i];
  if (el[0] > '0' && el[0] < '9') {
    pos++
    carpets.push([])
    continue
  }

  carpets[pos].push(el)
}

const vika = 'vika'

// for (let i = 0; i < 1; i++) {
for (let i = 0; i < carpets.length; i++) {
  const c = carpets[i]
  let target = 0

  // console.log(c)

  for (let j = 0; j < c[0].length; j++) {
    for (let jj = 0; jj < c.length; jj++) {
      const x = c[jj][j];
      
      // console.log("lf", vika[target])
      // console.log(x)

      if (x == vika[target]) {
        target++
        break
      }
      
    }
  }

  if (target >= 4) {
    res.push('yes')
  } else {
    res.push('no')
  }

}

console.log(res.join("\n"))
