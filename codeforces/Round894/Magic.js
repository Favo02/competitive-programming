var fs = require("fs")
var stdinBuffer = fs.readFileSync(0)
const input = stdinBuffer.toString().split("\n").splice(1)
input.pop()

const res = []

for (let i = 0; i < input.length; i+=3) {

  const f = input[i].split(" ")[0]
  const w = input[i].split(" ")[1]

  const monsters = input[i+2].split(" ").map(e => parseInt(e))
  const sum = monsters.reduce((ps, a) => ps + a, 0)

  // console.log(f,w,monsters)

  for (let s = 0; true; s++) {
    
    if (f*s + w*s >= sum) {
      // console.log("cp")
      if (checkPossible(monsters, f*s, w*s, false, false)) {
        res.push(s)
        break
      }

      if (checkPossible(monsters, f*s, w*s, true, false)) {
        res.push(s)
        break
      }

      if (checkPossible(monsters, f*s, w*s, false, true)) {
        res.push(s)
        break
      }

      if (checkPossible(monsters, f*s, w*s, true, true)) {
        res.push(s)
        break
      }
    }

  }
}
console.log(res.join("\n"))

function checkPossible(monsters, f, w, strat, strat2) {
  if (strat2) {
    monsters.sort().reverse()
  }
  // console.log(monsters, f, w)

  for (let i = 0; i < monsters.length; i++) {
    const m = monsters[i]

    if (strat) {
      if (f >= m && w >= m) {

        if (f > w) {
          w -= m
        }
        else {
          f -= m
        }

        if (f < 0 || w < 0) return false

      }
      else {
        strat = false
      }
    }

    if (!strat) {
      if (f > w) {
        f -= m
      }
      else {
        w -= m
      }

      if (f < 0 || w < 0) return false
    }
    

    

    
    
    // if (f > w) {
    //   f -= m
    // }
    // else {
    //   w -= m
    // }
  }

  return !(f < 0 || w < 0)
}
